import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import housing_data

def correlation_page_body():
    df = housing_data()
    st.write("## Correlation Analysis :bar_chart:")
    st.write(df.head(10))
    st.write("### Pearson & Spearman Correlation Plots")
    st.write("#### Pearson")
    pearson = plt.imread('/workspace/P5-Heritage-Housing/outputs/study/pearson.png')
    st.image(pearson)
    st.write("#### Spearman")
    spearman = plt.imread('/workspace/P5-Heritage-Housing/outputs/study/spearman.png')
    st.image(pearson)
    