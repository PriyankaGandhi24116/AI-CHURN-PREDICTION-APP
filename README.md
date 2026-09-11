# 🚀 AI-Powered Customer Churn Prediction & Explainable Analytics Dashboard

An AI-powered customer churn prediction application built using **Python, Machine Learning, Streamlit, Plotly, and SHAP**.

The application predicts whether a customer is likely to churn, provides the customer's churn probability and risk level, and explains the key factors influencing the prediction using **Explainable AI**.

> **Predict. Explain. Act. Retain.**

---

## 📌 Problem Statement

Customer churn can significantly impact business revenue, customer retention, and long-term growth.

Businesses need to identify customers who are likely to leave **before churn happens**. Traditional analysis may help identify patterns, but it may not provide real-time predictions or clearly explain why a particular customer is at risk.

---

## 💡 Solution

This project provides an interactive **Machine Learning-powered churn prediction dashboard** that helps businesses identify customers who are likely to leave.

The system analyzes customer information, generates a churn prediction, calculates the risk probability, and uses **SHAP Explainable AI** to identify the major factors influencing the prediction.

This allows businesses to move from:

> **Reactive Customer Retention → Proactive Customer Retention**

---

## ✨ Key Features

- 🎯 Real-time customer churn prediction
- 📊 Interactive analytics dashboard
- 📈 Churn and risk visualizations
- 🧠 SHAP-based Explainable AI
- 🔍 Customer-level risk analysis
- ⚡ Fast prediction results
- 📌 KPI metrics
- 📉 Customer churn insights
- 🎨 Interactive Streamlit interface

---

## 🏗️ System Architecture

```text
                 Customer Data
                       ↓
              Data Preprocessing
                       ↓
             Machine Learning Model
                       ↓
                Churn Prediction
                       ↓
                Risk Probability
                       ↓
              SHAP Explanation
                       ↓
               Business Insights
```

---

## 🔄 Project Workflow

```text
Data Collection
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Deployment
       ↓
Customer Input
       ↓
Churn Prediction
       ↓
Risk Analysis
       ↓
SHAP Explanation
```

---

## 🤖 Machine Learning

The application uses a **supervised Machine Learning classification approach** to predict customer churn.

### Input

Customer-related information such as:

- Customer demographics
- Account information
- Service usage
- Contract details
- Billing information
- Customer tenure
- Other relevant customer attributes

### Output

The system provides:

- **Churn / No Churn**
- **Churn Probability**
- **Risk Level**
- **Important Prediction Factors**

### Model

**Machine Learning Classification Model**

> Replace this with the exact ML model used in your project.

---

## 🧠 Explainable AI with SHAP

A major feature of this project is **Explainable AI**.

The application uses **SHAP (SHapley Additive exPlanations)** to understand the factors influencing individual predictions.

Instead of simply saying:

> **"This customer may churn."**

the system helps answer:

> **"Why is this customer likely to churn?"**

SHAP helps identify the customer features that contribute positively or negatively to the prediction.

This makes the Machine Learning model more:

- Transparent
- Interpretable
- Trustworthy
- Business-friendly

---

## 📊 Dashboard

The Streamlit dashboard provides an interactive interface for analyzing customer churn.

It includes:

- Customer information input
- Churn prediction
- Risk probability
- KPI cards
- Churn analytics
- Interactive charts
- Customer risk insights
- SHAP explanation visualizations

---

## 📸 Screenshots

### 🏠 Application Page

![Application Page](./APP%20PAGE.png)

### 📊 Dashboard

![Dashboard Page 1](./DASHBOARD%20PAGE%201.png)

![Dashboard Page 2](./DASHBOARD%20PAGE%202.png)

![Dashboard Page 3](./DASHBOARD%20PAGE%203.png)

### 🎯 Prediction

![Prediction Page 1](./PREDICTION%20PAGE%201.png)

![Prediction Page 2](./PREDICTION%20PAGE%202.png)

![Prediction Page 3](./PREDICTION%20PAGE%203.png)

---

## 🎬 How the Application Works

### Step 1 — Enter Customer Details

The user provides the required customer information through the Streamlit interface.

### Step 2 — Generate Prediction

The Machine Learning model processes the input and predicts whether the customer is likely to churn.

### Step 3 — Analyze Risk

The application displays:

- Churn status
- Churn probability
- Customer risk level

### Step 4 — Understand the Prediction

SHAP provides an explanation of the important factors influencing the prediction.

### Step 5 — Take Action

Businesses can use these insights to identify high-risk customers and develop proactive retention strategies.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application Development |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| SHAP | Explainable AI |
| Plotly | Interactive Visualization |
| Streamlit | Web Dashboard |

---

## 🎯 Business Value

The application can help businesses:

- Identify high-risk customers early
- Understand churn-driving factors
- Improve customer retention
- Support proactive retention strategies
- Reduce potential revenue loss
- Make data-driven decisions
- Prioritize customers based on risk

### Business Impact

```text
Customer Data
      ↓
Risk Identification
      ↓
Explain Churn Factors
      ↓
Proactive Action
      ↓
Improved Customer Retention
```

### 🔄 From Reactive to Proactive

> **Traditional Approach:** Customer leaves → Business reacts

> **Our Approach:** Predict risk → Understand why → Take action → Retain customer

---

## 🔍 Key Highlight

> **The system doesn't just predict customer churn — it explains why the customer may churn.**

The combination of:

**Prediction + Risk Analysis + Visualization + Explainability**

makes the application more useful for real-world business decision-making.

---

## 🚀 Future Enhancements

Planned improvements include:

- 🤖 AI-powered retention recommendations
- 🚨 Automated high-risk customer alerts
- ☁️ Cloud deployment
- 👥 Advanced customer segmentation
- 📧 Automated retention campaigns
- 📱 Mobile-friendly interface
- 📊 Advanced predictive analytics
- 🔄 Continuous model improvement

---

## 📁 Project Structure

```text
AI-CHURN-PREDICTION-APP/
│
├── APP PAGE.png
├── DASHBOARD PAGE 1.png
├── DASHBOARD PAGE 2.png
├── DASHBOARD PAGE 3.png
├── PREDICTION PAGE 1.png
├── PREDICTION PAGE 2.png
├── PREDICTION PAGE 3.png
│
├── app.py
├── dashboard.py
├── prediction.py
├── model.py
├── train_model.py
├── model.pkl
├── prediction_report (1).csv
├── config.toml
├── WA_Fn-UseC_-Telco-Customer-C...
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PriyankaGandhi24116/AI-CHURN-PREDICTION-APP.git
```

### 2. Navigate to the Project

```bash
cd AI-CHURN-PREDICTION-APP
```

### 3. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn plotly shap
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📦 Main Dependencies

```text
Python
Pandas
NumPy
Scikit-learn
SHAP
Plotly
Streamlit
```

---

## 🎥 Demo Flow

```text
Enter Customer Details
        ↓
      Predict
        ↓
Churn / No Churn
        ↓
Churn Probability
        ↓
Risk Level
        ↓
SHAP Explanation
        ↓
Business Insight
```

---

## 🏆 Project Highlights

### 🎯 Machine Learning

Uses supervised Machine Learning classification to predict the probability of customer churn.

### 🧠 Explainable AI

Uses SHAP to explain the factors influencing individual predictions.

### 📊 Interactive Dashboard

Uses Streamlit and Plotly to provide an interactive and visually engaging analytics experience.

### 💼 Business-Oriented Solution

Transforms Machine Learning predictions into actionable customer retention insights.

---

## 📝 Conclusion

This project demonstrates how **Machine Learning, Explainable AI, and interactive data visualization** can be combined to solve a real-world customer retention problem.

By combining:

**Prediction + Risk Analysis + Visualization + Explainability**

the application helps businesses understand customer churn and take proactive action.

> **Predict. Explain. Act. Retain.**

---

## 👩‍💻 Author

### Priyanka Gandhi

**Full Stack Developer | Microsoft Power BI Developer | AI/ML & Generative AI Enthusiast**

🔗 **GitHub:**  
https://github.com/PriyankaGandhi24116

🔗 **LinkedIn:**  
https://www.linkedin.com/in/priyanka-gandhi-b951b2436

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ **Star** on GitHub.

---

**Built with Python, Machine Learning, Explainable AI, Streamlit & Plotly.**
