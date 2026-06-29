from fastapi import FastAPI

app = FastAPI(
    title="Loan Prediction API",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message":
        "Loan Prediction ML Pipeline API"
    }


@app.get("/application-info")
def application_info():

    return {
        "project_name":
        "Loan Prediction System",

        "dataset_records":
        2000,

        "dataset_features":
        7,

        "problem_type":
        "Binary Classification"
    }


@app.get("/model-metrics")
def model_metrics():

    return {
        "model":
        "Random Forest",

        "accuracy":
        0.9933,

        "precision":
        1.0000,

        "recall":
        0.9612,

        "f1_score":
        0.9802
    }


@app.get("/pipeline-status")
def pipeline_status():

    return {
        "data_pipeline":
        "Completed",

        "dataops":
        "GitHub Actions",

        "mlops":
        "DagsHub + MLflow",

        "status":
        "Active"
    }


@app.get("/deployment-info")
def deployment_info():

    return {
        "cloud_provider":
        "Render",

        "api_framework":
        "FastAPI",

        "version":
        "1.0"
    }