import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Churn Dashboard", layout="wide")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- LOAD DATA ----------------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# ---------------- CSS ----------------
st.markdown("""
<style>
.main{
    background-color:#0E1117;
}
.kpi{
    background:#1E293B;
    padding:20px;
    border-radius:12px;
    text-align:center;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚀 AI Customer Churn Dashboard")
st.write("Real-Time Customer Churn Analytics using Machine Learning")

st.markdown("---")

# ---------------- KPI ----------------
total_customers = len(df)
churn_rate = (df["Churn"] == "Yes").mean() * 100
avg_monthly = df["MonthlyCharges"].mean()
avg_tenure = df["tenure"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Customers", total_customers)
c2.metric("⚠️ Churn Rate", f"{churn_rate:.2f}%")
c3.metric("💰 Avg Monthly", f"${avg_monthly:.2f}")
c4.metric("📅 Avg Tenure", f"{avg_tenure:.1f} Months")

st.markdown("---")

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

with col1:
    fig = px.pie(
        df,
        names="Churn",
        title="Customer Churn Distribution",
        hole=0.45
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.histogram(
        df,
        x="tenure",
        color="Churn",
        nbins=25,
        title="Tenure Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------- SCATTER ----------------
st.subheader("📊 Customer Segmentation")

fig = px.scatter(
    df,
    x="MonthlyCharges",
    y="TotalCharges",
    color="Churn",
    size="tenure",
    hover_data=["tenure"],
    title="Monthly Charges vs Total Charges"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- HEATMAP ----------------
st.subheader("🔥 Customer Density")

heat = px.density_heatmap(
    df,
    x="tenure",
    y="MonthlyCharges",
    title="Tenure vs Monthly Charges"
)

st.plotly_chart(heat, use_container_width=True)

st.markdown("---")

# ---------------- PREDICTION ----------------
st.header("🤖 Live AI Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.slider("Tenure", 0, 72, 12)

with col2:
    monthly = st.slider("Monthly Charges", 0, 150, 70)

with col3:
    total = st.slider("Total Charges", 0, 10000, 2000)

if st.button("🚀 Predict Churn"):

    input_data = pd.DataFrame({
        "tenure":[tenure],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability,
        title={"text":"Churn Risk"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"red"}
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

    if prediction == 1:
        st.error(f"🚨 High Churn Risk ({probability:.2f}%)")
    else:
        st.success(f"✅ Loyal Customer ({100-probability:.2f}%)")

    st.markdown("---")

    # ---------------- IMPACT ----------------
    st.subheader("💰 Business Impact")

    revenue = monthly * tenure
    ltv = revenue * 0.8

    a, b = st.columns(2)

    a.metric("Revenue Risk", f"${revenue:.2f}")
    b.metric("Lifetime Value", f"${ltv:.2f}")

    st.markdown("---")

    # ---------------- INSIGHTS ----------------
    st.subheader("🧠 AI Insights")

    if monthly > 80:
        st.warning("💸 High monthly charges increase churn risk.")

    if tenure < 12:
        st.warning("⏳ New customers are more likely to churn.")

    if total < 1000:
        st.warning("📉 Customer engagement is low.")

    st.markdown("---")

    # ---------------- FEATURE IMPORTANCE ----------------
    st.subheader("🧠 Explainable AI")

    importance = model.feature_importances_

    feature_df = pd.DataFrame({
        "Feature":[
            "Tenure",
            "Monthly Charges",
            "Total Charges"
        ],
        "Importance":importance
    })

    fig = px.bar(
        feature_df,
        x="Feature",
        y="Importance",
        color="Importance",
        text_auto=".2f",
        title="Feature Importance"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ---------------- RECOMMENDATIONS ----------------
    st.subheader("🎯 Smart Recommendations")

    if prediction == 1:

        if monthly > 80:
            st.write("✔ Offer a discount plan.")

        if tenure < 12:
            st.write("✔ Improve customer onboarding.")

        st.write("✔ Contact customer immediately.")
        st.write("✔ Offer loyalty rewards.")
        st.write("✔ Recommend annual subscription.")

    else:
        st.success("Customer is likely to stay.")
        st.write("✔ Upsell premium plans.")
        st.write("✔ Recommend additional services.")
        st.write("✔ Reward customer loyalty.")

st.markdown("---")

st.success("✅ AI Churn Dashboard Loaded Successfully")

st.markdown("""
<center>
<h4>💙 Built with Streamlit • Machine Learning • Plotly • AI</h4>
</center>
""", unsafe_allow_html=True)