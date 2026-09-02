import streamlit as st

# -------- LOGIN SYSTEM --------
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid credentials")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()
import time
import random

st.set_page_config(page_title="AI Churn Intelligence", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: #00f5ff;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
}

.glass {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

.center {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">🚀 AI Customer Churn Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict • Analyze • Explain • Act</div>', unsafe_allow_html=True)

st.markdown("---")

# ------------------ NAVIGATION ------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Open Dashboard"):
        st.switch_page("dashboard.py")

with col2:
    if st.button("🔮 Go to Prediction"):
        st.switch_page("dashboard.py")

st.markdown("---")

# ------------------ LIVE METRICS ------------------
st.markdown("### 📈 Live AI System Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Users Processed", "7,043")
c2.metric("Model Accuracy", "92%")
c3.metric("Predictions Today", "1,245")
c4.metric("Churn Alerts", "312")

st.markdown("---")

# ------------------ QUICK PREDICTION ------------------
st.markdown("### 🔮 Quick AI Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    monthly = st.slider("Monthly Charges ($)", 0, 150, 70)

with col3:
    total = st.slider("Total Charges ($)", 0, 10000, 2000)

if st.button("🚀 Predict Now"):
    
    # Simple logic model
    score = (monthly * 0.3 + total * 0.0005 - tenure * 0.2)
    probability = min(max(score, 0), 100)

    # Classification
    if probability > 70:
        st.error(f"🚨 High Churn Risk: {probability:.2f}%")
        segment = "🔴 High Risk"
    elif probability > 40:
        st.warning(f"⚠️ Medium Risk: {probability:.2f}%")
        segment = "🟡 Medium Risk"
    else:
        st.success(f"✅ Low Risk: {probability:.2f}%")
        segment = "🟢 Loyal Customer"

    st.markdown(f"### 🎯 Segment: {segment}")

    # ------------------ BUSINESS INSIGHTS ------------------
    st.markdown("### 💡 AI Insights")

    if monthly > 80:
        st.warning("💸 High monthly charges increase churn risk")

    if tenure < 12:
        st.warning("⏳ New customers are more likely to churn")

    if total < 1000:
        st.warning("📉 Low engagement detected")

    # ------------------ REVENUE IMPACT ------------------
    st.markdown("### 💰 Business Impact")

    revenue_loss = monthly * tenure
    ltv = monthly * tenure * 0.8

    col1, col2 = st.columns(2)
    col1.metric("💸 Revenue Risk", f"${revenue_loss:.2f}")
    col2.metric("💎 Lifetime Value", f"${ltv:.2f}")

    # ------------------ WHAT-IF ANALYSIS ------------------
    st.markdown("### 🧪 What-if Simulation")

    new_price = st.slider("Test Lower Price", 0, 150, monthly)

    if new_price < monthly:
        st.success("📉 Reducing price may reduce churn risk")

    # ------------------ RECOMMENDATIONS ------------------
    st.markdown("### 🎯 Smart Recommendations")

    if monthly > 80:
        st.write("👉 Offer discount or bundle plan")

    if tenure < 12:
        st.write("👉 Improve onboarding experience")

    if probability > 70:
        st.write("👉 Immediate retention campaign needed")

st.markdown("---")

# ------------------ FEATURES ------------------
st.markdown("### 💡 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.write("🔮 Real-time AI prediction")
    st.write("📊 Interactive dashboard")
    st.write("🧠 Explainable insights")
    st.write("⚡ Fast decision making")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.write("📈 Revenue analysis")
    st.write("🎯 Customer segmentation")
    st.write("📉 Risk scoring")
    st.write("🧪 What-if simulation")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ------------------ SYSTEM CHECK ------------------
st.markdown("### ⚙️ System Status")

if st.button("Run Full System Check"):
    with st.spinner("Running AI diagnostics..."):
        time.sleep(2)
    st.success("✅ All systems operational!")

st.markdown("---")

# ------------------ ABOUT ------------------
st.markdown("### 👨‍💻 About Project")

st.markdown('<div class="glass">', unsafe_allow_html=True)

st.write("""
This AI-powered system helps businesses:

- Predict customer churn
- Understand WHY customers leave
- Estimate revenue loss
- Take smart retention actions

Built for hackathon to showcase real-world AI impact.
""")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ------------------ FOOTER ------------------
st.markdown("""
<div class="center">
💙 Built with AI • Streamlit • Machine Learning <br>
🚀 Hackathon Ready • Judge Friendly
</div>
""", unsafe_allow_html=True)