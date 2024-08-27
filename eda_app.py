import streamlit as st
import pandas as pd
import seaborn as sns
from pandas_profiling import ProfileReport

# Title of the app
st.title('EDA with Pandas Profiling')

# Sidebar for data source selection
st.sidebar.header('Select Data Source')
data_source = st.sidebar.radio("Choose an option:", ["Upload CSV File", "Use Sample Data"])

if data_source == "Upload CSV File":
    # File uploader for user to upload a CSV file
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Load the data into a DataFrame
        data = pd.read_csv(uploaded_file)
        st.subheader('Uploaded Data')
        st.write(data.head())
else:
    # Option to select a sample dataset
    dataset_name = st.sidebar.selectbox("Choose a sample dataset:", ["Iris", "Titanic"])

    if dataset_name == "Iris":
        # Load the Iris dataset
        data = sns.load_dataset('iris')
    elif dataset_name == "Titanic":
        # Load the Titanic dataset
        data = sns.load_dataset('titanic')

    st.subheader(f'Sample Data - {dataset_name}')
    st.write(data.head())

# Create a ProfileReport for EDA
profile = ProfileReport(data, title="Pandas Profiling Report", explorative=True)
 
# Display the report
st.subheader('Pandas Profiling Report')
st_profile_report(profile)

# Function to render the pandas profiling report
def st_profile_report(profile):
    # Save the profile report as an HTML file
    profile_html = profile.to_html()
    st.components.v1.html(profile_html, height=1000, scrolling=True)
