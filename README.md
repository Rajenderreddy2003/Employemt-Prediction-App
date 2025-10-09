# 💼 Employment Prediction using Machine Learning

This project builds a **Decision Tree classification model** to predict whether an individual is employed or not, based on various personal, educational, and technical background attributes. A **Streamlit web app** is also developed for interactive data exploration and prediction.

---

## 📁 Dataset

- The dataset is sourced from an **open-source platform**.
- It contains records of individuals with attributes such as:
  - Age
  - Education Level
  - Employment Status
  - Main Branch (Tech/Non-Tech)
  - Mental Health Condition
  - Years of Coding Experience
  - Previous Salary
  - Computer Skills
  - Tools/Technologies worked with (`HaveWorkedWith`)

---

## 🎯 Objective

To analyze, preprocess, and model the data to **predict employment status (`Employed`)** using machine learning techniques, and present the process via an interactive Streamlit app.

---

## 🔍 Model Selection & Performance

Several machine learning algorithms were experimented with:

| Algorithm               | Accuracy |
|-------------------------|----------|
| Naive Bayes             | 0.772    |
| KNN Classifier          | 0.868    |
| Random Forest Classifier| 0.928    |
| **Decision Tree Classifier** ✅ | **0.999** |

The **Decision Tree Classifier** was chosen as the final model due to its superior accuracy and interpretability.

---

## 🛠️ Features & Workflow

### 1. 📄 Data Understanding
- Clear separation of **categorical**, **numerical**, and **target** features.
- Initial structure and statistics of the dataset visualized.

### 2. 📊 Exploratory Data Analysis (EDA)
- Distribution plots for numerical and categorical features.
- Target distribution visualization.
- Missing values handling:
  - `HaveWorkedWith` filled with `"Unknown"`.
- Applied **MultiLabelBinarizer** on `HaveWorkedWith`.

### 3. 🧠 Feature Engineering
- Removed unhelpful or redundant columns:
  - `YearsCodePro`, `Accessibility`, `Gender`
- Feature importance measured using **Mutual Information Classifier**.
- Applied encoding and scaling where necessary.

### 4. 🧪 Model Overview
- Built multiple models: Naive Bayes, KNN, Random Forest, and Decision Tree.
- Decision Tree achieved the **highest accuracy (0.999)**.
- Pipeline includes preprocessing, encoding, scaling, and prediction.

---

## 🚀 Streamlit App

The project is deployed as a **Streamlit web app**, providing:

- Problem Statement
- Data Understanding
- EDA Visualizations
- Feature Engineering Summary
- Model Overview
- Live Prediction Interface

---

## 🔗 Live Demo

Try the application live on **Hugging Face Spaces**:

👉 [Employment Prediction App](https://huggingface.co/spaces/Rajenderreddy2003/Employment_Prediction_App)

---

## 🧾 Requirements

Install all required packages usi
