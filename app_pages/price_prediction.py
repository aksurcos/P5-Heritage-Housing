import streamlit as st
import pandas as pd

from src.data_management import housing_data, load_pkl_file, inherited_house_data
from src.machine_learning.prediction import predict_sale_price

def price_prediction_page_body():
    
    pipeline = load_pkl_file("outputs/ml_pipeline/predict_SalePrice/v1/pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/v1/X_train.csv").columns.to_list())
    st.write("#### Meet Requirement: Four Inherited Houses")
    st.info(
		"The client is interested in predicting the house sale price"
		"from her four inherited houses in Ames, Iowa.\n\n"
		)

    in_df = inherited_house_data()
    features = ['GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    def display_house(house_num, house_data):
        with st.expander(f"🏠 House {house_num}", expanded=True):
            cols = st.columns([2, 1])
            
            with cols[0]:
                st.markdown("##### House Features:")
                for feature in features:
                    st.markdown(f"""
                        <div style='color: #3498DB; padding: 5px;'>
                            <strong>{feature}:</strong> {house_data[feature].values[0]}
                        </div>
                    """, unsafe_allow_html=True)
            
            with cols[1]:
                predict_sale_price(house_data, features, pipeline)

    
    houses = {
        1: in_df.iloc[[0]],
        2: in_df.iloc[[1]],
        3: in_df.iloc[[2]],
        4: in_df.iloc[[3]]
    }
    
    for num, house in houses.items():
        try:
            display_house(num, house)
        except Exception as e:
            st.error(f"Error displaying House {num}: {str(e)}")

    st.markdown("---")
    X_live = DrawInputsWidgets()
    
    if st.button('🎯Predict Sale Price'):
        st.write("**The Calculated Sale Price:**")
        predict_sale_price(X_live, sale_price_features, pipeline)

    


def DrawInputsWidgets():
    st.write("#### Meet Requirement: Other Houses' Sale Price")
    st.info(
		"The client is interested in predicting any other house's sale price. Only the most important variables that we have previously decided on can be selected."
    )
    df = housing_data
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)
    X_live = pd.DataFrame([], index=[0]) 
    with col1:
        feature = "OverallQual"
        st.markdown("##### 🏗️ Overall Quality")
        st_widget = st.number_input(
			label= 'Rate the overall material and finish (1-10)',
			min_value= 1, 
			max_value= 10,
            step = 1,
            help="Higher values indicate better quality"       
			)
        X_live[feature] = st_widget
        
    with col2:
        feature = "GrLivArea"
        st.markdown("##### 🏠 Living Area")
        st_widget = st.number_input(
			label= 'Above grade living area (sq ft between 334-5642)',
			min_value= 334,
			max_value= 5642, 
            step= 10,
            help="Total square feet of above grade living area"
			)
        X_live[feature] = st_widget
        
    with col3:
        feature = "TotalBsmtSF"
        st.markdown("##### 🏠︎ Basement Area")
        st_widget = st.number_input(
			label= 'Total basement area (sq ft between 0-6110)',
			min_value= 0,
			max_value= 6110, 
            step= 10,
            help="Total square feet of basement area"
			)
        X_live[feature] = st_widget
        
    with col4:
        feature = "GarageArea"
        st.markdown("##### 🚗 Garage Area")
        st_widget = st.number_input(
			label= "Size of garage (sq ft between 0-1418)",
			min_value= 0,
			max_value= 1418, 
            step= 10,
            help="Total square feet of garage area"
			)
        X_live[feature] = st_widget
        
    with col5:
        feature = "YearBuilt"
        st.markdown("##### 📅 Year Built")
        st_widget = st.number_input(
			label= "Construction year between 1872-2010", 
			min_value= 1872,
			max_value= 2010,
            step= 1,
            help="Original construction date"
			)
        X_live[feature] = st_widget
        
        return X_live




