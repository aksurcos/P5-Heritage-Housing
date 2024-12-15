import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def machine_learning_page_body():
    st.write("## Machine Learning Model Performance")

    st.write("### Model Comparison")
    st.info("After testing 3 models, we've decided that regression without feature engineering model gave the best results after making comparisons. You can check the details below and Jupyter Notebooks.")

    st.write("The regression without feature engineering model is better because: \n\n "
            "- More balanced performance between train and test sets \n\n"
            "- Better generalization \n\n"
            "- More reliable predictions on unseen data \n\n"
            "- Less overfitting \n\n"
            "- It shows more robust and reliable performance. \n\n"
            )


     
    st.write("### Model Performance Metrics")
    model_performance = {
        'Set': ['TrainSet', 'TestSet'],
        'R2 Score': [0.901, 0.86],
        'Mean Absolute Error': [17614.303, 19424.068],
        'Mean Squared Error': [610931610.731, 966526052.289],
        'Root Mean Squared Error': [24717.031, 31089.002]
    }
    st.dataframe(model_performance)

    models_comparison = {
        'Model': ['ExtraTreesRegressor', 'LinearRegression', 'RandomForestRegressor', 'GradientBoostingRegressor', 'XGBRegressor'],
        'mean_score': [0.804695, 0.786672, 0.785848, 0.754929, 748435]
    }
    st.dataframe(models_comparison)
    
    st.write("#### Actual vs Predicted Values Analysis")
    st.write("""
    The scatter plots demonstrate the relationship between actual and predicted house prices 
    for both training and test datasets. The red diagonal line represents perfect predictions.
    """)
    predictions = plt.imread('/workspace/P5-Heritage-Housing/outputs/study/predictions.png')
    st.image(predictions)
    st.write("""
    **Key Observations:**
    - Strong correlation between actual and predicted values
    - Model performs consistently across both training and test sets
    - Slightly higher variance in predictions for high-value properties
    """)

    st.write("#### Feature Importance Analysis")
    
    st.write("""
    The feature importance graph highlights which characteristics of a house 
    have the most significant impact on its price prediction.
    """)
    
    feature_imp = {
        'Feature': ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'YearBuilt', 'GarageArea'],
        'Importance': [0.50, 0.27, 0.09, 0.08, 0.06]
    }
    
    fig = px.bar(
        feature_imp, 
        x='Feature', 
        y='Importance',
        title='Feature Importance in Price Prediction'
    )
    
    st.plotly_chart(fig)
    
    st.write("""
    **Key Observations:**
    - Overall Quality is the dominant factor in price prediction
    - Living Area is the second most important feature
    - The top two features account for 77% of the model's predictive power
    - Basement, Year Built, and Garage Area have lesser but still notable impact
    """)


