import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import housing_data

def correlation_page_body():
    df = housing_data()
    st.write("## Correlation Analysis :bar_chart:")
    st.write(df.head(10))
    