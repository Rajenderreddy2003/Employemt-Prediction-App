import streamlit as st
import pickle
import pandas as pd

input_columns = ['Age', 'EdLevel', 'Employment', 'MentalHealth', 'MainBranch', 'YearsCode', 'PreviousSalary', 'ComputerSkills', 'APL', 'ASP.NET', 'ASP.NET Core ', 'AWS', 'Angular', 'Angular.js', 'Ansible', 'Assembly', 'Bash/Shell', 'Blazor', 'C', 'C#', 'C++', 'COBOL', 'Cassandra', 'Chef', 'Clojure', 'Cloud Firestore', 'Colocation', 'CouchDB', 'Couchbase', 'Crystal', 'Dart', 'Delphi', 'Deno', 'DigitalOcean', 'Django', 'Docker', 'Drupal', 'DynamoDB', 'Elasticsearch', 'Elixir', 'Erlang', 'Express', 'F#', 'FastAPI', 'Fastify', 'Firebase', 'Firebase Realtime Database', 'Flask', 'Flow', 'Fortran', 'Gatsby', 'Git', 'Go', 'Google Cloud', 'Google Cloud Platform', 'Groovy', 'HTML/CSS', 'Haskell', 'Heroku', 'Homebrew', 'IBM Cloud or Watson', 'IBM DB2', 'Java', 'JavaScript', 'Julia', 'Kotlin', 'Kubernetes', 'LISP', 'Laravel', 'Linode', 'Lua', 'MATLAB', 'Managed Hosting', 'MariaDB', 'Matlab', 'Microsoft Azure', 'Microsoft SQL Server', 'MongoDB', 'MySQL', 'Neo4j', 'Next.js', 'Node.js', 'Nuxt.js', 'OCaml', 'OVH', 'Objective-C', 'OpenStack', 'Oracle', 'Oracle Cloud Infrastructure', 'PHP', 'Perl', 'Phoenix', 'Play Framework', 'PostgreSQL', 'PowerShell', 'Pulumi', 'Puppet', 'Python', 'R', 'React.js', 'Redis', 'Ruby', 'Ruby on Rails', 'Rust', 'SAS', 'SQL', 'SQLite', 'Scala', 'Solidity', 'Spring', 'Svelte', 'Swift', 'Symfony', 'Terraform', 'TypeScript', 'Unity 3D', 'Unknown', 'Unreal Engine', 'VBA', 'VMware', 'Vue.js', 'Xamarin', 'Yarn', 'jQuery', 'npm']

# Load model pipeline and required input columns
with open("nb_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Employment Predictor", layout="centered")
st.title("💼 Employment Status Prediction")
st.markdown("Fill out the details to predict if a person is employed.")

# User input fields (with updates applied)
user_input = {
    "Age": st.selectbox("Age", ["<35", ">35"]),
    "EdLevel": st.selectbox("Education Level", ['Other', 'Undergraduate', 'Master', 'NoHigherEd', 'PhD']),
    "Employment": st.selectbox("Current Employment Status", [0, 1]),  # 0 = Not Working, 1 = Working
    "MentalHealth": st.selectbox("Mental Health Condition", ["Yes", "No"]),
    "MainBranch": st.selectbox("Main Branch", ["Dev", "NotDev"]),
    "YearsCode": st.slider("Years of Coding Experience", 0, 50, 5),
    "PreviousSalary": st.number_input("Previous Salary", min_value=0, max_value=4_000_00, value=50000),
    "ComputerSkills": st.slider("Computer Skills ", 0, 107, 8)
}

# Extract tech-related features from the training column list
tech_features = [col for col in input_columns if col not in user_input.keys()]

# Tech skills multiselect
selected_skills = st.multiselect("Technologies Used", tech_features)

# Add selected skill flags to user input
for tech in tech_features:
    user_input[tech] = 1 if tech in selected_skills else 0

# Create input DataFrame
input_df = pd.DataFrame([user_input])

if st.button("Back to Model Overview"):
    st.switch_page("pages/5_Model Overview.py")

# Predict button
if st.button("Predict Employment Status"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success(f"Prediction: Employed")
    else:
        st.warning(f"Prediction: Not Employed")
