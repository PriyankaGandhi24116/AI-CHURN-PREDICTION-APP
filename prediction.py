import streamlit as st
import pandas as pd
import pickle
import cv2
import numpy as np
from PIL import Image
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Customer Churn Prediction",
    page_icon="🤖",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- TITLE ----------------
st.title("🤖 AI Customer Churn Prediction")
st.markdown("### Predict customer churn using Machine Learning")

st.markdown("---")

# ---------------- IMAGE UPLOAD ----------------
st.subheader("📷 Customer Image")

uploaded_image = st.file_uploader(
    "Upload Customer Photo",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Customer", width=250)

    st.success("✅ Image uploaded successfully")

st.markdown("---")

# ---------------- CUSTOMER DETAILS ----------------
st.subheader("📋 Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    monthly = st.slider("Monthly Charges ($)", 0, 150, 70)

with col3:
    total = st.slider("Total Charges ($)", 0, 10000, 2000)

st.markdown("---")

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict Churn"):

    input_df = pd.DataFrame({
        "tenure":[tenure],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1] * 100

    st.subheader("🎯 Prediction Result")

    if prediction == 1:
        st.error(f"🚨 High Churn Risk ({probability:.2f}%)")
    else:
        st.success(f"✅ Loyal Customer ({100-probability:.2f}%)")

    st.markdown("---")

    # ---------------- RISK METER ----------------
    st.subheader("📊 Churn Risk")

    st.progress(int(probability))

    st.metric(
        "Prediction Probability",
        f"{probability:.2f}%"
    )

    st.markdown("---")

    # ---------------- BUSINESS INSIGHTS ----------------
    st.subheader("💡 AI Insights")

    if monthly > 80:
        st.warning("💸 High Monthly Charges increase churn risk.")

    if tenure < 12:
        st.warning("⏳ New customers are more likely to churn.")

    if total < 1000:
        st.warning("📉 Low customer engagement detected.")

    if monthly <= 80 and tenure >= 24:
        st.success("😊 Customer appears stable.")

    st.markdown("---")

    # ---------------- BUSINESS IMPACT ----------------
    st.subheader("💰 Business Impact")

    revenue = monthly * tenure
    ltv = revenue * 0.8

    c1, c2 = st.columns(2)

    c1.metric("Revenue Risk", f"${revenue:.2f}")
    c2.metric("Estimated Lifetime Value", f"${ltv:.2f}")

    st.markdown("---")

    # ---------------- CUSTOMER SEGMENT ----------------
    st.subheader("📌 Customer Segment")

    if probability >= 80:
        segment = "🔴 Critical Risk"
    elif probability >= 60:
        segment = "🟠 High Risk"
    elif probability >= 40:
        segment = "🟡 Medium Risk"
    else:
        segment = "🟢 Loyal"

    st.info(segment)

    st.markdown("---")

    # ---------------- AI RECOMMENDATIONS ----------------
    st.subheader("🎯 Smart Recommendations")

    if prediction == 1:

        st.error("Retention Actions")

        st.write("✔ Offer discount")
        st.write("✔ Provide loyalty rewards")
        st.write("✔ Contact customer immediately")
        st.write("✔ Recommend annual contract")
        st.write("✔ Assign dedicated relationship manager")

    else:

        st.success("Growth Opportunities")

        st.write("✔ Upsell premium services")
        st.write("✔ Offer referral rewards")
        st.write("✔ Loyalty bonus points")
        st.write("✔ Promote family plans")

    st.markdown("---")

    # ---------------- PREDICTION SUMMARY ----------------
    st.subheader("📄 Prediction Summary")

    summary = pd.DataFrame({

        "Parameter":[
            "Tenure",
            "Monthly Charges",
            "Total Charges",
            "Prediction",
            "Probability",
            "Revenue Risk",
            "Lifetime Value"
        ],

        "Value":[
            tenure,
            monthly,
            total,
            "Churn" if prediction == 1 else "No Churn",
            f"{probability:.2f}%",
            f"${revenue:.2f}",
            f"${ltv:.2f}"
        ]

    })

    st.dataframe(summary, use_container_width=True)

    # ---------------- DOWNLOAD REPORT ----------------
    csv = summary.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction Report",
        data=csv,
        file_name="prediction_report.csv",
        mime="text/csv"
    )

st.markdown("---")
st.success("✅ AI Prediction System Ready")