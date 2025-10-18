import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Employment_Data.csv")

# Page title
st.title("Data Understanding")

# Intro description
st.markdown("""
### Dataset Overview

This dataset, sourced from an **open-source platform**, contains records of individuals with various demographic, educational, and technical attributes.  
The goal is to predict whether a person is **employed** or **unemployed** based on their background, skills, and experience.  

We experimented with several machine learning algorithms, including:
- Naive Bayes
- KNN Classifier
- Random Forest Classifier
- **Decision Tree Classifier** (final model used for its highest accuracy)
""")

# Section: Dataset Features
st.markdown("""
### Dataset Features:

#### Categorical Features:
- **Age**: Age group (e.g., '<35', '>35')
- **EdLevel**: Highest education level (e.g., 'Undergraduate', 'Master', 'PhD')
- **MentalHealth**: Mental health condition reported ('Yes' or 'No')
- **MainBranch**: Primary professional domain (e.g., 'Dev', 'NotDev')

#### Numerical Features:
- **Employment**: Employment indicator (not the target)
- **YearsCode**: Total years of coding experience
- **PreviousSalary**: Last known salary
- **ComputerSkills**: Score representing computer proficiency

#### Target Variable:
- **Employed**: Current employment status (1 = Employed, 0 = Unemployed)
""")

# Show sample data
st.markdown("### Sample Records")
st.dataframe(df[['Age', 'EdLevel', 'Employment', 'MentalHealth', 'MainBranch', 'YearsCode', 'PreviousSalary', 'ComputerSkills', 'Employed']].head())

if st.button("Back to Problem Statement"):
    st.switch_page("pages/1_Problem Statement.py")

if st.button("Next Page"):
    st.switch_page("pages/3_EDA.py")