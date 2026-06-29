# src/train.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def prepare_data(df):

    X = df.drop(
        columns=[
            "Loan_Approved",
            "Income_Category"
        ],
        errors="ignore"
    )

    y = df["Loan_Approved"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.30,
            random_state=42,
            stratify=y
        )
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )

def train_logistic_regression(
    X_train,
    y_train
):

    model = LogisticRegression()

    model.fit(
        X_train,
        y_train
    )

    return model

def train_random_forest(
    X_train,
    y_train
):

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model

