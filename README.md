# Loan Prediction ML Pipeline - Cloud-Based Data Science Application

## Project Overview

This project implements an end-to-end Cloud-Based Data Science and Machine Learning application for Loan Approval Prediction. The objective is to automate data processing, model training, monitoring, and API access using modern DataOps and MLOps practices.

The project uses a publicly available Loan Prediction dataset and demonstrates the complete machine learning lifecycle, including data ingestion, preprocessing, exploratory data analysis (EDA), model training, model evaluation, workflow automation, experiment tracking, and API deployment.

---

## Business Problem

Financial institutions need to determine whether a loan application should be approved based on an applicant's profile. Manual evaluation can be time-consuming and inconsistent.

The goal of this project is to build a machine learning system that predicts loan approval status based on customer attributes such as:

* Age
* Income
* Credit Score
* Loan Amount
* Loan Term
* Employment Status

The prediction helps automate loan approval decisions and improve operational efficiency.

---

## Dataset Information

Dataset Source: Kaggle

Dataset Name: Loan Prediction Dataset
Dateset URl: https://www.kaggle.com/datasets/mosaadhendam/loan-prediction-dataset

Features:

| Feature           | Description           |
| ----------------- | --------------------- |
| Age               | Applicant Age         |
| Income            | Applicant Income      |
| Credit_Score      | Credit Score          |
| Loan_Amount       | Requested Loan Amount |
| Loan_Term         | Loan Duration         |
| Employment_Status | Employment Category   |
| Loan_Approved     | Target Variable       |

Dataset Statistics:

* Number of Records: 2000
* Number of Features: 7
* Missing Values: 0

---

# Project Architecture

Kaggle Dataset

↓

Data Ingestion

↓

Data Preprocessing

↓

Exploratory Data Analysis (EDA)

↓

GitHub Actions (DataOps)

↓

Machine Learning Training

↓

DagsHub + MLflow (MLOps)

↓

FastAPI Application

↓

Render Cloud Deployment

---

# Project Structure

```text
loan-prediction-project/

├── .github/
│   └── workflows/
│       └── data_pipeline.yml
│
├── api/
│   └── main.py
│
├── data/
│   └── raw/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── screenshots/
│
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── train.py
│   ├── evaluate.py
│   ├── run_pipeline.py
│   └── mlops_tracking.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Project Stages

## Stage 1: Business Understanding

* Identified loan approval prediction as the business problem.
* Defined project objectives and expected outcomes.

---

## Stage 2: Data Ingestion

* Downloaded dataset from Kaggle.
* Loaded dataset using Pandas.
* Verified schema and dataset integrity.

Activities:

* Data loading
* Shape verification
* Dataset inspection

---

## Stage 3: Data Preprocessing

Performed multiple preprocessing operations:

* Missing value verification
* Data type inspection
* Categorical feature encoding
* Feature scaling using normalization
* Feature engineering

Generated Features:

* Income_Per_Loan
* Loan_Burden

---

## Stage 4: Exploratory Data Analysis (EDA)

Performed comprehensive data analysis:

### Univariate Analysis

* Distribution of Age
* Distribution of Income
* Distribution of Loan Amount

### Bivariate Analysis

* Income vs Loan Approval
* Credit Score vs Loan Approval

### Correlation Analysis

* Correlation matrix
* Heatmap visualization

### Feature Engineering Analysis

* Income binning
* Loan burden analysis

---

## Stage 5: DataOps Implementation

Data pipeline automation was implemented using:

### GitHub Actions

Workflow Activities:

* Data ingestion
* Data preprocessing
* EDA execution
* Logging
* Artifact generation

Benefits:

* Automated execution
* Cloud-based workflow
* Centralized logs
* Reproducibility

---

## Stage 6: Machine Learning Pipeline

### Algorithms Used

1. Logistic Regression
2. Random Forest Classifier

### Data Split

* Training Data: 70%
* Testing Data: 30%

---

## Stage 7: Model Evaluation

### Logistic Regression

* Accuracy: 91.33%
* Precision: 83.12%
* Recall: 62.14%
* F1 Score: 71.11%

### Random Forest

* Accuracy: 99.33%
* Precision: 100.00%
* Recall: 96.12%
* F1 Score: 98.02%

### Best Model

Random Forest Classifier

Reason:

* Highest Accuracy
* Highest F1 Score
* Better Generalization

---

## Stage 8: MLOps Implementation

Implemented experiment tracking using:

* MLflow
* DagsHub

Tracked Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

Tracked Artifacts:

* Trained Model
* Experiment Metadata
* Run Information

Benefits:

* Model monitoring
* Experiment reproducibility
* Performance tracking
* Cloud-based monitoring

---

## Stage 9: API Development

Developed REST APIs using FastAPI.

Available Endpoints:

### Home Endpoint

```http
GET /
```

### Application Information

```http
GET /application-info
```

### Model Metrics

```http
GET /model-metrics
```

### Pipeline Status

```http
GET /pipeline-status
```

### Deployment Information

```http
GET /deployment-info
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Stage 10: Cloud Deployment

The FastAPI application was deployed on Render.

Cloud Components Used:

* GitHub
* GitHub Actions
* DagsHub
* Render

This provides a complete cloud-based machine learning application.

---

# Technologies Used

Programming Language:

* Python

Libraries:

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* FastAPI
* MLflow
* DagsHub

Cloud Platforms:

* GitHub
* GitHub Actions
* DagsHub
* Render

---

# Key Results

| Metric    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 91.33%              | 99.33%        |
| Precision | 83.12%              | 100.00%       |
| Recall    | 62.14%              | 96.12%        |
| F1 Score  | 71.11%              | 98.02%        |

Selected Model: Random Forest Classifier

---

# Learning Outcomes

This project provided hands-on experience in:

### Data Engineering

* Data ingestion
* Data preprocessing
* Feature engineering

### Data Analysis

* Exploratory Data Analysis
* Statistical analysis
* Data visualization

### Machine Learning

* Classification algorithms
* Model evaluation
* Performance comparison

### DataOps

* Workflow automation
* Scheduled execution
* Cloud logging

### MLOps

* Experiment tracking
* Model monitoring
* MLflow integration

### API Development

* REST API design
* FastAPI development
* Swagger documentation

### Cloud Computing

* GitHub Actions
* DagsHub
* Render deployment

---

# Project Summary

This project successfully developed a cloud-based end-to-end machine learning application for loan approval prediction. The solution incorporates DataOps for automated data processing, MLOps for experiment tracking and monitoring, and FastAPI for API access. The application was deployed using cloud services and achieved an accuracy of 99.33% using a Random Forest Classifier.

The project demonstrates the complete lifecycle of a modern machine learning system, from data ingestion to cloud deployment, following industry-standard practices for Data Science, DataOps, and MLOps.

