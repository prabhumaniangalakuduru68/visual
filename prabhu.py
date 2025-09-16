import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title("Visualization App - Roll No: 23ME1A5472")

file = st.file_uploader("Upload CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.write("### Data Preview", df.head())

    chart_type = st.selectbox("Choose Visualization", ["Line", "Bar", "Scatter", "Histogram"])

    if chart_type == "Line":
        st.line_chart(df)
    elif chart_type == "Bar":
        st.bar_chart(df)
    elif chart_type == "Scatter":
        x = st.selectbox("X-axis", df.columns)
        y = st.selectbox("Y-axis", df.columns)
        st.write(alt.Chart(df).mark_circle().encode(x=x, y=y))
    elif chart_type == "Histogram":
        col = st.selectbox("Select Column", df.columns)
        fig, ax = plt.subplots()
        ax.hist(df[col].dropna(), bins=20)
        st.pyplot(fig)
