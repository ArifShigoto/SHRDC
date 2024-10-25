import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('banking.csv')

st.title("Page 1: Banking Dataset Overview")

# Create controls for filtering the charts
selected_job = st.selectbox("Select Job Type", df['job'].unique())
selected_education = st.selectbox("Select Education Level", df['education'].unique())

# Create two columns
col1, col2 = st.columns(2)

# Interactive chart 1 with control (filtered by selected job)
with col1:
    st.subheader(f"Age Distribution for Job: {selected_job}")
    filtered_data_job = df[df['job'] == selected_job]
    age_chart = px.histogram(filtered_data_job, x='age', title=f"Age Distribution for {selected_job}")
    st.plotly_chart(age_chart)

# Interactive chart 2 with control (filtered by selected education)
with col2:
    st.subheader(f"Euribor 3-Month Rate for Education: {selected_education}")
    filtered_data_education = df[df['education'] == selected_education]
    euribor_chart = px.histogram(filtered_data_education, x='euribor3m', title=f"Euribor Rate for {selected_education}")
    st.plotly_chart(euribor_chart)
