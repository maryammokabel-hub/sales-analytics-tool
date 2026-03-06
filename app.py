import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.analyzer import analyze_sales
from src.charts import create_charts
from src.report_generator import generate_report


st.title("Sales Analytics Tool")

uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:

    # load data
    df = load_data(uploaded_file)

    st.subheader("Raw Data")
    st.write(df)

    # clean data
    df = clean_data(df)

    st.subheader("Cleaned Data")
    st.write(df)

    # analysis
    summary = analyze_sales(df)

    st.subheader("Sales Summary")
    st.write(summary)

    # charts
    st.subheader("Charts")
    fig = create_charts(df)
    st.pyplot(fig)

    # report
    if st.button("Generate PDF Report"):
        generate_report(summary)
        st.success("Report generated successfully!")