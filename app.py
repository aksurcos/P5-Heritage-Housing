import streamlit as st
from app_pages.multipage import MultiPage

# Load Pages Scripts
st.set_page_config(
    page_title="Heritage House Project",
    page_icon="🏚️"
)

from app_pages.summary_page import summary_page_body
from app_pages.hypothesis_page import hypothesis_page_body
from app_pages.correlation_page import correlation_page_body
from app_pages.price_prediction import price_prediction_page_body
from app_pages.machine_learning import machine_learning_page_body


app = MultiPage(app_name= "Heritage House Project :house:") #App Name

# Add your app pages here using .add_page()
app.add_page("Summary :house:", summary_page_body)
app.add_page("Hypothesis :pencil:", hypothesis_page_body)
app.add_page("Correlation Analysis :bar_chart:", correlation_page_body)
app.add_page("House Price Prediction :moneybag:", price_prediction_page_body)
app.add_page("Machine Learning Model :robot_face:", machine_learning_page_body)


# Run the  app
app.run() 