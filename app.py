import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_approval_model.pkl")

st.title("Loan Approval Prediction")
st.write("Enter applicant details to predict whether the loan is likely to be approved.")
gender = st.selectbox("Gender", ["Male", "Female"])

married = st.selectbox("Married", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0.0,
    value=0.0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=150.0
)

loan_term = st.selectbox(
    "Loan Amount Term",
    [360.0, 180.0, 120.0, 84.0, 60.0, 36.0, 12.0]
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)
if st.button("Predict Loan Approval"):

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]

rejection_probability = probabilities[0]
approval_probability = probabilities[1]

st.write(f"Rejection Probability: {rejection_probability:.2%}")
st.write(f"Approval Probability: {approval_probability:.2%}")

if prediction == "Y":
    st.success("Loan is likely to be APPROVED.")
else:
    st.error("Loan is likely to be REJECTED.")