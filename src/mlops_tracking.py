import dagshub
import mlflow
import sys
import os

dagshub.init(
    repo_name="loan-prediction-mlops",
    repo_owner="2024ad05357",
    mlflow=True
)

sys.path.append(os.path.abspath("..")) 

from train import *
from evaluate import *
from ingestion import *
from preprocessing import *

df = load_data(
    "data/raw/loan_prediction_dataset.csv"
)

df = encode_categorical(df)

df = create_features(df)

df = normalize_features(df)

(
    X_train,
    X_test,
    y_train,
    y_test
) = prepare_data(df)

rf_model = train_random_forest(
    X_train,
    y_train
)

results = evaluate_model(
    rf_model,
    X_test,
    y_test,
    "Random Forest"
)

with mlflow.start_run():

    mlflow.log_param(
        "model",
        "RandomForest"
    )

    mlflow.log_metric(
        "accuracy",
        results["accuracy"]
    )

    mlflow.log_metric(
        "precision",
        results["precision"]
    )

    mlflow.log_metric(
        "recall",
        results["recall"]
    )

    mlflow.log_metric(
        "f1_score",
        results["f1"]
    )

    mlflow.sklearn.log_model(
        rf_model,
        "random_forest_model"
    )

print("\nModel metrics logged successfully to DagsHub.")