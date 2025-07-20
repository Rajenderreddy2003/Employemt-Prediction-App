import streamlit as st

# Page title
st.title("🧠 Model Overview")

# Introduction to Naive Bayes
st.markdown("""
### 📌 Naive Bayes Classifier

This project uses a **Naive Bayes Classifier**, a probabilistic algorithm based on **Bayes' Theorem** with the assumption of conditional independence between features.

It is particularly effective for structured data involving both categorical and numerical variables.
""")

# Features and target
st.header("🛠️ Model Inputs & Target")

st.markdown("""
**Input Features Used for Training:**
- `Age`
- `EdLevel`
- `Employment`
- `MentalHealth`
- `MainBranch`
- `YearsCode`
- `PreviousSalary`
- `ComputerSkills`

**Target Variable:**
- `Employed` — Binary classification:  
  - `1` → Employed  
  - `0` → Unemployed
""")

# Why Naive Bayes
st.header("🤔 Why Naive Bayes?")
st.markdown("""
- ⚡ **Fast & efficient** on large datasets  
- ✅ Handles both categorical & numerical data  
- 💡 Works well even when some features are less informative  
- 🧮 Ideal for baseline models due to simplicity and speed

Given the dataset’s nature, Naive Bayes was a suitable and reliable choice.
""")

# Model task
st.header("📊 Classification Task")
st.markdown("""
The goal is to build a **binary classification model** to predict whether an individual is currently **employed** based on background, education, and technical profile.
""")

# Accuracy score
st.header("📈 Model Performance")
st.markdown("""
The **Naive Bayes classifier** achieved an accuracy of:

### 🎯 **0.77** (77%)

This indicates that the model correctly predicted employment status for 77% of the records in the test set.
""")

if st.button("Back to Feature Engineering"):
    st.switch_page("pages/4_Feature Engineering.py")

if st.button("Next Page"):
    st.switch_page("pages/6_Model Prediction.py")