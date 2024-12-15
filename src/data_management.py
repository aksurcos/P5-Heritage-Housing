import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache_resource
def housing_data():
    df = pd.read_csv("outputs/datasets/collection/cleaned/CleanedHousePrices.csv")
    return df

def inherited_house_data():
    in_df = pd.read_csv("outputs/datasets/collection/inherited_houses.csv")
    return in_df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)