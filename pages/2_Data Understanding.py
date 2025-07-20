import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Employment_Data.csv")

# Page title
st.title("🔍 Data Understanding")

# Intro description
st.markdown("""
### 📄 Dataset Overview

This dataset, sourced from an **open-source platform**, contains records of individuals with various demographic and technical attributes.  
The goal is to predict whether a person is **employed** or **unemployed** based on their background, skills, and experience.  
A **Naive Bayes classifier** is being built using this data.
""")

# Section: Dataset Features
st.markdown("""
### 🗂️ Dataset Features:

#### ✅ Categorical Features:
- **Age**: Age group of the individual (e.g., `<35`, `>35`)
- **EdLevel**: Highest education level attained (e.g., `Undergraduate`, `Master`, `PhD`)
- **MentalHealth**: Mental health condition reported by the individual (`Yes` or `No`)
- **MainBranch**: Primary professional domain (e.g., `Dev`, `NotDev`)

#### ✅ Numerical Features:
- **Employment**: A numerical indicator of employment condition (not the target)
- **YearsCode**: Total years of coding experience (e.g., `7`, `15`, `40`)
- **PreviousSalary**: Last known salary before current status
- **ComputerSkills**: A numeric score representing computer proficiency

#### 🎯 Target Variable:
- **Employed**: Indicates current employment status (`1` = Employed, `0` = Unemployed)
""")

# Show sample data
st.markdown("### 📊 Sample Records")
st.dataframe(df[['Age', 'EdLevel', 'Employment', 'MentalHealth', 'MainBranch', 'YearsCode', 'PreviousSalary', 'ComputerSkills', 'Employed']].head())

if st.button("Back to Problem Statement"):
    st.switch_page("pages/1_Problem Statement.py")

if st.button("Next Page"):
    st.switch_page("pages/3_EDA.py")