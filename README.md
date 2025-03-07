# azureml-pipelines

# XGBoost Model Deployment using Docker

## Overview
This branch focuses on retrieving a registered XGBoost model from the Azure Machine Learning model registry, creating a Docker image of the model, and testing the Docker container locally.

## Steps Covered
1. **Retrieve the Registered Model**: Fetch the XGBoost model from Azure ML model registry using SDK v2.
2. **Create a Docker Image**: Package the model into a Docker container.
3. **Test the Docker Image Locally**: Deploy the container and run inference.

## Prerequisites
- Azure CLI installed and logged in
- Azure ML SDK v2 (`azure.ai.ml`)
- Docker installed and running
- Python 3.8+
- Required dependencies installed (`pip install -r requirements.txt`)

## Steps to Execute

- **Download the Model**: The model can be retrieved from Azure ML using `download_model.py`.
- **Create Docker Image**: The Docker image is built and configured for deployment.
- **Test the Model**: The model can be tested using `test.py`.

## Conclusion
This branch provides a streamlined approach to fetching a registered XGBoost model from Azure, containerizing it using Docker, and testing it locally before deploying it in a production environment.

For further enhancements, CI/CD integration and cloud deployment can be added.

## Author
Akash Namdeo

---

