# src/eda.py

import os
from narwhals import corr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

def summary_statistics(df):

    print("\nSummary Statistics")
    print(df.describe())

    return df.describe()

import os

def correlation_analysis(df):

    corr = df.corr()

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm"
    )

    plt.title(
        "Correlation Matrix"
    )

    os.makedirs(
        "../reports",
        exist_ok=True
    )

    plt.savefig(
        "../reports/correlation_heatmap.png"
    )

    plt.close()

    return corr

def create_income_bins(df):

    df = df.copy()

    df["Income_Category"] = pd.cut(
        df["Income"],
        bins=3,
        labels=[
            "Low",
            "Medium",
            "High"
        ]
    )

    print(
        df["Income_Category"]
        .value_counts()
    )

    return df

def target_distribution(df):

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Loan_Approved",
        data=df
    )

    plt.title(
        "Loan Approval Distribution"
    )

    plt.show()

def univariate_analysis(df):

    numeric_cols = [
        "Age",
        "Income",
        "Credit_Score",
        "Loan_Amount"
    ]

    for col in numeric_cols:

        plt.figure(figsize=(6,4))

        sns.histplot(
            df[col],
            kde=True
        )

        plt.title(col)

        plt.show()

def employment_analysis(df):

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Employment_Status",
        data=df
    )

    plt.title(
        "Employment Status"
    )

    plt.show()

def bivariate_analysis(df):

    columns = [
        "Income",
        "Credit_Score",
        "Age"
    ]

    for col in columns:

        plt.figure(figsize=(6,4))

        sns.boxplot(
            x="Loan_Approved",
            y=col,
            data=df
        )

        plt.title(
            f"{col} vs Loan Approval"
        )

        plt.show()

def feature_importance(df):

    X = df.drop(
        columns=["Loan_Approved"]
    )

    y = df["Loan_Approved"]

    model = RandomForestClassifier(
        random_state=42
    )

    model.fit(X, y)

    importance = pd.DataFrame(
        {
            "Feature": X.columns,
            "Importance":
            model.feature_importances_
        }
    )

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    plt.figure(figsize=(8,5))

    sns.barplot(
        x="Importance",
        y="Feature",
        data=importance
    )

    plt.title(
        "Feature Importance"
    )

    plt.show()

    return importance