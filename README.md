# 🔧 Predictive Maintenance using Machine Learning

> An end-to-end Machine Learning project that predicts potential machine failures from operating conditions and provides the prediction through a Flask web application.

## 🚀 Live Demo

🌐 **[Launch the Predictive Maintenance App](https://machine-maintance-project.onrender.com)**

## 💻 GitHub Repository

📂 **[View Source Code](https://github.com/shaikmudassir850/machine-maintance-proj)**

---

## 📌 About the Project

Machine failures can lead to unexpected downtime, production delays, equipment damage, and increased maintenance costs.

This project demonstrates how **Machine Learning can be used for predictive maintenance** by analyzing machine operating conditions and predicting whether a machine is likely to experience a failure.

The project follows a complete end-to-end Machine Learning workflow:

**Data → Preprocessing → EDA → Model Training → Evaluation → Model Saving → Flask → Deployment**

The trained Machine Learning model is integrated into a Flask web application where users can enter machine parameters and receive a prediction through an interactive interface.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Understand and analyze machine operating data.
- Clean and prepare the dataset for Machine Learning.
- Perform Exploratory Data Analysis (EDA).
- Identify relevant features for prediction.
- Encode categorical variables.
- Split data into training and testing sets.
- Apply feature scaling where required.
- Train multiple classification algorithms.
- Compare model performance.
- Select an appropriate final model.
- Save the trained model and scaler.
- Build a Flask web application.
- Deploy the application online.
- Provide an easy-to-use interface for machine failure prediction.

---

# 💼 Business Problem

Unexpected equipment failure is a major challenge in industrial environments.

A machine that suddenly stops working can result in:

- Production downtime
- Lost productivity
- Emergency repair costs
- Equipment damage
- Delayed orders
- Increased maintenance expenses

Traditional maintenance can be performed in two common ways.

### Preventive Maintenance

Maintenance is performed at fixed intervals.

**Limitation:** A machine may be maintained even when it is still operating normally.

### Reactive Maintenance

Maintenance is performed after the machine fails.

**Limitation:** The failure has already caused downtime and potentially expensive damage.

### Predictive Maintenance

Predictive maintenance attempts to identify potential problems **before a failure occurs**.

```text
Machine Operating Conditions
             ↓
      Machine Learning Model
             ↓
      Failure Prediction
             ↓
   Maintenance Investigation
             ↓
      Preventive Action
