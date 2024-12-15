import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from src.data_management import housing_data

def correlation_page_body():
    df = housing_data()
    st.write("## Correlation Analysis :bar_chart:")
    st.write(df.head(10))
    st.write("### Pearson & Spearman Correlation Plots")
    st.write("#### Pearson")
    pearson = plt.imread('outputs/study/pearson.png')
    st.image(pearson)
    
    
    st.write("#### Spearman")
    spearman = plt.imread('outputs/study/spearman.png')
    st.image(spearman)
    

    positive_corr = [
        '1stFlrSF: First floor square feet', 
        'GarageArea', 
        'GrLivArea: Above grade (ground) living area square feet',
        'OverallQual: Overall Quality',  
        'TotalBsmtSF: Total square feet of basement area', 
        'YearBuilt',
        ]
    st.write("##### The correlation study shows that SalePrice has positive correlation with this variables:")
    st.write(positive_corr)
    negative_corr = [
            'KitchenQual_TA: Kitchen Quality Typical/Average', 
            'GarageFinish_Unf: Garage is Unfinished',
            'MasVnrArea_0.0: Masonry veneer area 0.0 in square feet',
            'GarageYrBlt_Missing: Garage Year Built Missing',
            'GarageFinish_None: Garage is Not finished'
        ]
    st.write("##### The correlation study shows that SalePrice has negative correlation with this variables:")
    st.write(negative_corr)
    st.write("#### Scatterplot Graph of Variables (which has positive correlation with SalePrice")
    scatter = plt.imread('outputs/study/scatter.png')
    st.image(scatter)
    st.write("##### What the scatterplot graph tells:\n"
        "- **1:** We see that as First floor area expands, the price increases.\n"
        "- **2:** Sale price generally increases with garage area (GarageArea).\n"
        "- **3:** There's a strong positive relationship between living area (GrLivArea) and price.\n"
        "- **4:** Overall quality (OverallQual) shows a clear positive correlation with price.\n"
        "- **5:** Total basement area (TotalBsmtSF) has a positive relationship with price.\n"
        "- **6:** Year built (YearBuilt) shows that newer houses tend to have higher prices.\n"
    )
    

    



