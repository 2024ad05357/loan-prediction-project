# src/ingestion.py

import pandas as pd


def load_data(filepath):
    """
    Load dataset from CSV file.
    """

    df = pd.read_csv(filepath)

    print("=" * 50)
    print("Dataset Loaded Successfully")
    print("=" * 50)

    print(f"Shape: {df.shape}")

    return df


def dataset_overview(df):
    """
    Display dataset overview.
    """
    print("The dataset has total", df.isnull().sum().sum(), "missing values.")

    print("=" * 50)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())
    print("=" * 50)

