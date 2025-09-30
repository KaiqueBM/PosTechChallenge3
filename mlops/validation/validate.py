import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()
model_name = "car_features_model"

# Buscar a última versão do modelo no estágio "None"
latest = client.get_latest_versions(model_name, stages=["None"])
run_id = latest[0].run_id
metrics = client.get_run(run_id).data.metrics

# Verificar o threshold de R² para a métrica "msrp_r2"
if metrics.get("msrp_r2", 0) < 0.5:
    raise ValueError("Modelo não passou no threshold de R² para msrp")
