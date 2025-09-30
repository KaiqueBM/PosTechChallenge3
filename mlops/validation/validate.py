import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()
model_name = "car_features_model"

latest = client.get_latest_versions(model_name, stages=["None"])
run_id = latest[0].run_id
metrics = client.get_run(run_id).data.metrics

if metrics.get("MSRP_r2", 0) < 0.5:
    raise ValueError("Modelo não passou no threshold de R² para MSRP")