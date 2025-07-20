import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Employment_Data.csv")

# Define features
categorical_columns = ['Age', 'EdLevel', 'MentalHealth', 'MainBranch']
numerical_columns = ['YearsCode', 'PreviousSalary', 'ComputerSkills']
target_column = 'Employed'

# Page title
st.title("📊 Exploratory Data Analysis (EDA)")

st.markdown("""
This page provides an overview of the dataset structure, handles missing values, 
and explores the distribution of key features to inform modeling choices.
""")

# Dataset overview
st.header("📁 Dataset Overview")
st.write(f"**Rows:** {df.shape[0]}")
st.write(f"**Columns:** {df.shape[1]}")

# Column classification
st.subheader("🧩 Feature Classification")
st.markdown(f"- **Categorical Features:** {', '.join(categorical_columns)}")
st.markdown(f"- **Numerical Features:** {', '.join(numerical_columns)}")
st.markdown(f"- **Target Variable:** {target_column}")

# Unique values in categorical
st.subheader("🔢 Unique Values in Categorical Columns")
for col in categorical_columns:
    st.write(f"**{col}** — {df[col].nunique()} unique values: {df[col].unique()}")

# Missing value check
st.header("🚨 Missing Values Check")
missing = df.isnull().sum()
missing = missing[missing > 0]

if not missing.empty:
    st.write("Columns with missing values:")
    st.dataframe(missing.rename("Missing Count"))

    st.subheader("🧼 Missing Value Handling Strategy")
    st.markdown("""
    - The **HaveWorkedWith** column contained missing values.
    - These were filled with the value `"Unknown"` to retain data integrity.
    - Then, the column was processed using **MultiLabelBinarizer** to convert multi-skill responses into binary features for modeling.
    """)
else:
    st.success("✅ No missing values detected in the dataset.")

# Target variable
st.header("🎯 Target Variable Distribution: Employed")
fig, ax = plt.subplots()
sns.countplot(data=df, x=target_column, palette="Set2", ax=ax)
ax.set_xticklabels(["Unemployed (0)", "Employed (1)"])
ax.set_ylabel("Count")
ax.set_title("Employment Status Distribution")
st.pyplot(fig)

# Categorical plots
st.header("📌 Categorical Feature Distributions")
for col in categorical_columns:
    st.subheader(col)
    fig, ax = plt.subplots()
    sns.countplot(data=df, x=col, palette="pastel", ax=ax)
    ax.set_title(f"Distribution of {col}")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Numerical plots
st.header("📈 Numerical Feature Distributions")
for col in numerical_columns:
    st.subheader(col)
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, color="skyblue", ax=ax)
    ax.set_title(f"Distribution of {col}")
    st.pyplot(fig)


if st.button("Back to Data Understanding"):
    st.switch_page("pages/2_Data Understanding.py")

if st.button("Next Page"):
    st.switch_page("pages/4_Feature Engineering.py")