# 💼 Employment Prediction using Naive Bayes

This project builds a Naive Bayes classification model to predict whether an individual is employed or not, based on various personal, educational, and technical background attributes. A Streamlit web app is also developed for interactive data exploration and prediction.

---

## 📁 Dataset

- The dataset used is sourced from an **open-source platform**.
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

To analyze, preprocess, and model the data to **predict employment status (`Employed`)** using machine learning techniques, and present the entire process via an interactive Streamlit app.

---

## 🛠️ Features & Workflow

### 1. 📄 Data Understanding
- Clear separation of **categorical**, **numerical**, and **target** features.
- Initial structure and statistics of the dataset are visualized.

### 2. 📊 Exploratory Data Analysis (EDA)
- Distribution plots for numerical and categorical features.
- Target distribution visualization.
- Missing values handling:
  - `HaveWorkedWith` filled with `"Unknown"`.
- Applied **MultiLabelBinarizer** on `HaveWorkedWith`.

### 3. 🧠 Feature Engineering
- Removed unhelpful or redundant columns:
  - `YearsCodePro`, `Accessibility`, and `Gender`
- Feature importance measured using **Mutual Information Classifier**.
- Applied encoding and scaling where necessary.

### 4. 🧪 Model Overview
- Used a **Naive Bayes Classifier** to predict `Employed`.
- Achieved an **accuracy of 0.77** on evaluation.
- Clean pipeline from preprocessing to prediction.

---

## 🚀 Streamlit App

The project is deployed as a **Streamlit web app**, which provides:

- Introduction and Problem Statement
- Data Understanding
- EDA Visualizations
- Feature Engineering Summary
- Model Overview
- Live Prediction

---

## 🧾 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
