import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("Employment_Data.csv")

# Page title
st.title("🛠️ Feature Engineering")

# Intro
st.markdown("""
Feature engineering is the process of transforming raw data into meaningful features that improve model performance.  
For this project, we prepared the dataset for training a **Naive Bayes classifier** by applying a variety of preprocessing techniques.
""")

# Section: Categorical Encoding
st.header("🔤 Handling Categorical Features")
st.markdown("""
The following features were identified as categorical and were encoded appropriately:

- **Age**: Ordinal values like `<35`, `>35` encoded numerically  
- **EdLevel**: Educational levels (`Undergraduate`, `Master`, `PhD`) were encoded using **Ordinal Encoding**  
- **MentalHealth**: Binary (`Yes` / `No`) encoded as 0 and 1  
- **MainBranch**: Encoded using **Label Encoding** or **One-Hot Encoding** based on model compatibility  
""")

# Section: Numerical Scaling
st.header("📐 Scaling Numerical Features")
st.markdown("""
Numerical features were scaled to normalize their impact on the model:

- **YearsCode**: Number of years of general coding experience  
- **PreviousSalary**: Highly skewed, scaled using **RobustScaler**  
- **ComputerSkills**: Already a numerical skill score; optionally scaled  
""")

# Section: Feature Selection
st.header("📌 Feature Selection & Cleanup")
st.markdown("""
To enhance the model’s performance and eliminate noise, the following steps were applied:

- **Mutual Information Classifier** was used to assess feature relevance
- Based on low mutual information with the target, the following columns were removed:
  - `YearsCodePro`
  - `Accessibility`
  - `Gender`

- **Employment** column was retained as a valid numerical input  
- **Employed** was kept as the **target variable**
""")

# Show preview of selected feature columns
st.subheader("🧾 Final Feature Subset (First 5 Rows)")
selected_columns = ['Age', 'EdLevel', 'Employment', 'MentalHealth', 'MainBranch', 'YearsCode', 'PreviousSalary', 'ComputerSkills', 'Employed']
st.dataframe(df[selected_columns].head())

if st.button("Back to EDA"):
    st.switch_page("pages/3_EDA.py")

if st.button("Next Page"):
    st.switch_page("pages/5_Model Overview.py")