# Fraud Detection ML System

End-to-end Machine Learning system for detecting fraudulent credit card transactions.

## Tech Stack
- Python
- XGBoost
- FastAPI
- MLflow
- Docker
- Streamlit
- Scikit-learn

## Project Structure

fraud-detection-ml-system
│
├── api
│   └── app.py
│
├── data
│
├── notebooks
│   └── fraud_model_training.ipynb
│
├── models
│
├── dashboard
│
├── logs
│
├── Dockerfile
├── requirements.txt
└── README.md

## Dataset

The dataset is not stored in this repository due to GitHub file size limits.

Download from Kaggle:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

After downloading, place the file here:

data/creditcard.csv

## Run API

uvicorn api.app:app --reload

Open:

http://127.0.0.1:8000/docs

## Run Dashboard

streamlit run dashboard/dashboard.py
