# src/preprocessing.py

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


def check_missing_values(df):

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df.isnull().sum()


def encode_categorical(df):

    df = df.copy()

    categorical_cols = df.select_dtypes(include=["object"]).columns

    encoder = LabelEncoder()

    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    return df


def create_features(df):

    df = df.copy()

    df["Income_Per_Loan"] = (
        df["Income"] / df["Loan_Amount"]
    )

    df["Loan_Burden"] = (
        df["Loan_Amount"] / df["Income"]
    )

    return df


def normalize_features(df):

    df = df.copy()

    scaler = MinMaxScaler()

    numeric_cols = [
        col for col in df.columns
        if col != "Loan_Approved"
    ]

    df[numeric_cols] = scaler.fit_transform(
        df[numeric_cols]
    )

    return df