import mlflow
import pandas as pd
from datetime import datetime

def predict_batch(model_uri, input_path, output_path, model_version):
    """
    Batch inference usando pandas e modelo scikit-learn registrado no MLflow.
    
    Args:
        model_uri: URI do modelo no MLflow (ex: models:/car_features_model/1)
        input_path: caminho de entrada (CSV ou Delta -> aqui simplificamos para CSV)
        output_path: caminho de saída (CSV ou Delta)
        model_version: versão do modelo (para log)
    """
    # Carregar modelo
    model = mlflow.sklearn.load_model(model_uri)

    # Ler dataset
    df = pd.read_csv(input_path)

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

    # Salvar em CSV
    final_df.to_csv(output_path, index=False)
    print(f"Predições salvas em: {output_path}")
