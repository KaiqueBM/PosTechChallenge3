import mlflow
import pandas as pd
from datetime import datetime

def predict_batch(spark, model_uri, source_table, output_table, model_version):
    """
    Batch inference usando pandas e modelo scikit-learn registrado no MLflow.
    
    Args:
        model_uri: URI do modelo no MLflow (ex: models:/car_features_model/1)
        source_table: tabela da source
        output_table: tabela dos resultados
        model_version: versão do modelo (para log)
    """
    # Carregar modelo
    model = mlflow.sklearn.load_model(model_uri)

    # Ler dataset
    df_raw = spark.read.table(source_table)
    df = df_raw.toPandas()

    # Features (remove colunas alvo)
    X = df.drop(columns=["msrp", "city_mpg", "highway_mpg"], errors="ignore")

    # Fazer previsões
    preds = model.predict(X)

    # Montar DF final com previsões
    pred_df = pd.DataFrame(
        preds,
        columns=["msrp_pred", "city_mpg_pred", "highway_mpg_pred"]
    )
    final_df = pd.concat([df.reset_index(drop=True), pred_df], axis=1)

    # Adicionar metadados
    final_df["model_id"] = model_version
    final_df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Salvar Resultados Na Tabela
    spark_df = spark.createDataFrame(final_df)
    spark.sql("create database if not exists postech_ml")
    spark_df.write.mode("append").saveAsTable(output_table)
