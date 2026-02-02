
# 🚗 Insurance Claim Prediction App

🔗 **Live App:**
👉 https://retailpriceoptimizationprediction-yvikw2vcybononj9ixdaoe.streamlit.app/

---

## 📌 Project Overview

This project is a **machine learning–based web application** that predicts whether an insurance claim is likely to occur based on customer and policy details.

The goal is to make **insurance risk prediction simple and understandable**, even for users with **zero machine learning knowledge**.

The app is built using:

* **XGBoost** for prediction
* **Streamlit** for a beginner-friendly frontend

---

## 🎯 Key Features

* ✅ Extremely **beginner-friendly UI**
* ✅ No need to know exact values — sliders & dropdowns provided
* ✅ Clear explanations for every input
* ✅ Real-time prediction results
* ✅ Feature importance visualization
* ✅ Handles **imbalanced data effectively**
* ✅ Deployed and accessible online

---

## 🧠 Machine Learning Model

* **Algorithm:** XGBoost Classifier
* **Problem Type:** Binary Classification (Claim / No Claim)
* **Evaluation Metrics Used:**

  * MAE (Mean Absolute Error)
  * RMSE (Root Mean Squared Error)
  * R² Score
* **Imbalance Handling:** Class weighting & model tuning

---

## 🖥️ User Interface (Frontend)

The app is designed assuming users:

* ❌ Do NOT know ML
* ❌ Do NOT know exact feature values

### UI Highlights:

* Sliders instead of raw numbers
* Dropdowns for categorical values
* Yes/No toggles
* “I’m not sure” default options
* Plain-English explanations under every input
* Organized sections (Personal Info, Vehicle Info, Policy Info, etc.)

---

## 📊 Prediction Output

Instead of technical numbers, users see:

* 🔮 **Prediction:** High / Low chance of claim
* 📊 **Confidence Level:** Low / Medium / High
* 📈 **Feature Importance Chart:** Explains *why* the model predicted that result

---

## 📁 Project Structure

```
├── app.py                  # Streamlit application
├── model.pkl               # Trained XGBoost model
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── data/                   # Dataset (if applicable)
```

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd insurance-claim-prediction
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This project is deployed using **Streamlit Cloud**.

🔗 **Live Application:**
👉 https://retailpriceoptimizationprediction-yvikw2vcybononj9ixdaoe.streamlit.app/

---

## 👩‍💻 Author

**Krishna Gangeya Karbhari**
Graduate BE Computer Science Engineering student
Interested in **AI, ML, Data Science & Analytics**

---

## ⭐ Acknowledgements

* Streamlit
* Scikit-learn
* XGBoost
* Open-source ML community

