import os

from ingestion import load_data
from preprocessing import (
    check_missing_values,
    encode_categorical,
    create_features,
    normalize_features
)
from eda import (
    summary_statistics,
    correlation_analysis,
    create_income_bins
)

print("Starting Data Pipeline")

print("=" * 50)
print("Create Reports Directory")
os.makedirs(
    "reports",
    exist_ok=True
)
print("Reports Directory Created Successfully")

df = load_data("data/raw/loan_prediction_dataset.csv")

check_missing_values(df)

df = encode_categorical(df)

df = create_features(df)

df = normalize_features(df)

summary_statistics(df)

correlation_analysis(df)

create_income_bins(df)

print("Pipeline Completed Successfully")