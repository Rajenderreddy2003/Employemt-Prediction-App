import streamlit as st

st.set_page_config(page_title="Employment Predictor", layout="centered")

st.title("💼 Employment Prediction App")
st.markdown("""
Welcome to the **Employment Predictor**!

This application uses a **Naive Bayes Machine Learning model** trained on real-world survey data to predict whether a person is likely to be **employed** based on their:

- 🧠 Mental health and background
- 💻 Technical and computer skills
- 🎓 Education level
- 💼 Work experience and salary history
- ⚙️ Technologies and tools they know

---

### How to Use:
1. Fill in the form with accurate information.
2. Select the technologies you are familiar with.
3. Click **Predict** to see your employment prediction.

---

This tool is ideal for:
- Job seekers
- Career advisors
- HR data analysts
- Anyone curious about how skills relate to employment!

""")

if st.button("Next Page"):
    st.switch_page("pages/1_Problem Statement.py")