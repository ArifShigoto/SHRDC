import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('banking.csv')

st.title("Page 2: Banking Dataset Trends")

# Create controls for filtering the charts
age_range = st.slider("Select Age Range", int(df['age'].min()), int(df['age'].max()), (30, 60))
selected_marital_status = st.selectbox("Select Marital Status", df['marital'].unique())

# Filter the dataframe based on controls
filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) & (df['marital'] == selected_marital_status)]

# Create two columns
col1, col2 = st.columns(2)

# Interactive chart 1 with control (filtered by age and marital status)
with col1:
    st.subheader(f"Job Distribution for Ages {age_range[0]}-{age_range[1]}")
    job_chart = px.histogram(filtered_df, x='job', title=f"Job Distribution for Ages {age_range[0]}-{age_range[1]}")
    st.plotly_chart(job_chart)

# Interactive chart 2 with control (filtered by age and marital status)
with col2:
    st.subheader(f"Campaigns for Marital Status: {selected_marital_status}")
    campaign_chart = px.scatter(filtered_df, x='age', y='campaign', title=f"Campaigns by Age for {selected_marital_status}")
    st.plotly_chart(campaign_chart)
