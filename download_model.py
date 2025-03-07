from azure.ai.ml import MLClient, Input, Output, command
from azure.identity import DefaultAzureCredential
import os
# Connect to Azure ML workspace
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
workspace_name = os.getenv("AZURE_WORKSPACE_NAME")

# Authenticate with Azure using Managed Identity
credential = DefaultAzureCredential()
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

# Get the model from Azure
model_name = "xgboost_model_1741284243"
model_version = 1  # Change as needed

model = ml_client.models.get(name=model_name, version=model_version)

# Download model locally
local_model_path = "./model"
os.makedirs(local_model_path, exist_ok=True)

ml_client.models.download(name=model_name, version=model_version, download_path=local_model_path)

print(f"✅ Model downloaded to {local_model_path}")
