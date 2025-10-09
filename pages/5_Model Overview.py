import streamlit as st

# Page title
st.title("🧠 Model Overview")

# Introduction to Decision Tree
st.markdown("""
### 📌 Model Selection Overview

We experimented with several machine learning algorithms to predict employment status:

| Algorithm               | Accuracy |
|-------------------------|----------|
| Naive Bayes             | 0.772    |
| KNN Classifier          | 0.868    |
| Random Forest Classifier| 0.928    |
| **Decision Tree Classifier** ✅ | **0.999** |

The **Decision Tree Classifier** was chosen as the final model due to its superior accuracy on this dataset.
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

# Why Decision Tree
st.header("🤔 Why Decision Tree?")
st.markdown("""
- ⚡ **Extremely high accuracy** (0.999) compared to other models  
- ✅ Handles both categorical & numerical features  
- 💡 Captures complex relationships between features  
- 🧮 Easy to interpret and visualize  

Given these advantages, the Decision Tree was selected as the most reliable model for predicting employment status.
""")

# Model task
st.header("📊 Classification Task")
st.markdown("""
The goal is to build a **binary classification model** to predict whether an individual is currently **employed** based on their background, education, and technical profile.
""")

if st.button("Back to Feature Engineering"):
    st.switch_page("pages/4_Feature Engineering.py")

if st.button("Next Page"):
    st.switch_page("pages/6_Model Prediction.py")