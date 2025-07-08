import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")
client = MlflowClient()

print("Current Tracking URI:", mlflow.get_tracking_uri())

try:
    model_name = "wine_quality_model"
    versions = client.get_latest_versions(model_name)
    print(f"\nAvailable versions for '{model_name}':")
    for v in versions:
        print(f"Version: {v.version}, Run ID: {v.run_id}, Current Stage: {v.current_stage}")
except Exception as e:
    print("❌ Error while fetching model versions:", e)
