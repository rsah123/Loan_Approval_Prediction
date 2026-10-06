# Loan Approval Prediction

A machine learning classification project that predicts whether a loan application is likely to be approved or rejected based on applicant and loan-related information.

## Features Used

- Gender
- Marital Status
- Dependents
- Education
- Self Employment
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

## Dataset

The dataset contains 614 loan applications.

Target:
- Y = Loan Approved
- N = Loan Rejected

The dataset contains missing values in several numerical and categorical features.

## Data Preprocessing

A reproducible scikit-learn pipeline was used for preprocessing.

Numerical features:
- Missing values filled using median imputation
- Features scaled using StandardScaler

Categorical features:
- Missing values filled using most frequent value
- One-hot encoding applied using OneHotEncoder

## Models Compared

- Logistic Regression
- Decision Tree
- Random Forest
- Balanced Logistic Regression

## Model Performance

| Model | Accuracy | Approved F1-score |
|---|---:|---:|
| Logistic Regression | 86.18% | 90.81% |
| Balanced Logistic Regression | 82.93% | 87.72% |
| Decision Tree | 75.61% | 82.35% |
| Random Forest | 82.11% | 87.50% |

Logistic Regression was selected as the final model based on overall performance.

## Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Streamlit
- Joblib

## Project Structure

```text
Loan_Approval_Prediction/
│
├── data/
├── notebook/
│   └── loan_approval.ipynb
├── app.py
├── loan_approval_model.pkl
├── requirements.txt
├── README.md
└── .gitignore