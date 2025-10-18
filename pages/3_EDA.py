import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Employment_Data.csv")

# -------------------- Data Cleaning --------------------
# Remove unnamed index or placeholder columns such as "Unnamed: 0"
removed_columns = []
if any(df.columns.str.contains('^Unnamed')):
    removed = df.loc[:, df.columns.str.contains('^Unnamed')].columns.tolist()
    removed_columns.extend(removed)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Drop irrelevant column
if 'Country' in df.columns:
    df.drop(columns=['Country'], inplace=True)
    removed_columns.append('Country')

# Check for duplicates
duplicate_count = df.duplicated().sum()
if duplicate_count > 0:
    df.drop_duplicates(inplace=True)

# -------------------- Define Features --------------------
categorical_columns = ['Age', 'EdLevel', 'MentalHealth', 'MainBranch','Employment']
numerical_columns = ['YearsCode', 'PreviousSalary']  # Removed ComputerSkills
target_column = 'Employed'

# Page title
st.title("Exploratory Data Analysis (EDA)")

st.markdown("""
This page provides an overview of the dataset structure, handles missing values, 
and explores the distribution of key features to inform modeling choices.
""")

# Dataset overview
st.header("Dataset Overview")
st.write(f"**Rows:** {df.shape[0]}")
st.write(f"**Columns:** {df.shape[1]}")
if removed_columns:
    st.write(f"Removed columns during cleaning: {', '.join(removed_columns)}")
if duplicate_count > 0:
    st.write(f"Removed {duplicate_count} duplicate rows from the dataset.")

# Column classification
st.subheader("Feature Classification")
st.markdown(f"- **Categorical Features:** {', '.join(categorical_columns)}")
st.markdown(f"- **Numerical Features:** {', '.join(numerical_columns)}")
st.markdown(f"- **Target Variable:** {target_column}")

# Unique values in categorical
st.subheader("Unique Values in Categorical Columns")
for col in categorical_columns:
    st.write(f"**{col}** — {df[col].nunique()} unique values: {df[col].unique()}")

# Missing value check
st.header("Missing Values Check")
missing = df.isnull().sum()
missing = missing[missing > 0]

if not missing.empty:
    st.write("Columns with missing values:")
    st.dataframe(missing.rename("Missing Count"))
else:
    st.success("No missing values detected in the dataset.")

# Target variable
st.header("Target Variable Distribution: Employed")
fig, ax = plt.subplots()
sns.countplot(data=df, x=target_column, palette="Set2", ax=ax)
ax.set_xticklabels(["Unemployed (0)", "Employed (1)"])
ax.set_ylabel("Count")
ax.set_title("Employment Status Distribution")
st.pyplot(fig)

# Categorical plots
st.header("Categorical Feature Distributions")
for col in categorical_columns:
    st.subheader(col)
    fig, ax = plt.subplots()
    sns.countplot(data=df, x=col, palette="pastel", ax=ax)
    ax.set_title(f"Distribution of {col}")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Numerical plots
st.header("Numerical Feature Distributions")
for col in numerical_columns:
    st.subheader(col)
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, color="skyblue", ax=ax)
    ax.set_title(f"Distribution of {col}")
    st.pyplot(fig)

# Correlation Heatmap
st.header("Correlation Heatmap")
heatmap_df = df.select_dtypes(include=['int64', 'float64'])
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(heatmap_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Correlation Heatmap of Numerical Features")
st.pyplot(fig)

# Navigation
if st.button("Back to Data Understanding"):
    st.switch_page("pages/2_Data Understanding.py")

if st.button("Next Page"):
    st.switch_page("pages/4_Feature Engineering.py")
