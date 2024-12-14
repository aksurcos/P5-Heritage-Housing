import streamlit as st


def summary_page_body():
    st.write("## Project Overview and Requirements")
    st.info("Our client requested our help in order to optimize the sale price of four inherited residences in Ames, Iowa. In order to provide the most accurate price indication for the inherited property, a machine learning model and regression methods were developed.")
    st.write("### Requirements")
    st.write("- The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that."
    "- The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/aksurcos/P5-Heritage-Housing).")
