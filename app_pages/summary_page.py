import streamlit as st


def summary_page_body():
    st.write("## Project Overview and Requirements ")
    st.info("Our client requested our help in order to optimize the sale price of four inherited residences in Ames, Iowa. In order to provide the most accurate price indication for the inherited property, a machine learning model and regression methods were developed.")
    st.info(
        """
        This project helps property owners:
        * Understand how different house attributes affect sale prices
        * Predict house prices based on various features
        """
    )
    st.write("### Requirements")
    st.write("- The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.")
    st.write("- The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/aksurcos/P5-Heritage-Housing).")

    st.write("---")
    st.write("## Explanation of Variables")
    st.write("#### The More Important Variables For Our Project\n"
        "- **SalePrice** is our target variable.\n"
        "- **1stFlrSF**: First floor square feet\n"
        "- **GrLivArea**: Above grade (ground) living area square feet\n"
        "- **GarageYrBlt**: Year garage was built\n"
        "- **TotalBsmtSF**: Total square feet of basement area\n"
        "- **GarageArea**: Size of garage in square feet\n"
        "- **YearBuilt**: Original construction date\n"
    )
    
    if st.checkbox("Click to see all variables."):
        st.write(
            "- **2ndFlrSF**: Second floor square feet\n\n"
            "- **BedroomAbvGr**: Bedrooms above grade (does NOT include basement bedrooms)\n"
            "- **BsmtExposure**: Refers to walkout or garden level walls\n"
            "   - Gd: Good Exposure;\n"
            "   - Av: Average Exposure;\n"
            "   - Mn: Mimimum Exposure;\n"
            "   - No: No Exposure;\n"
            "   - None: No Basement\n\n"
            "- **BsmtFinType1**: Rating of basement finished area\n\n"
            "   - GLQ: Good Living Quarters;\n"
            "   - ALQ: Average Living Quarters;\n"
            "   - BLQ: Below Average Living Quarters;\n"
            "   - Rec: Average Rec Room;\n"
            "   - LwQ: Low Quality;\n"
            "   - Unf: Unfinshed;\n"
            "   - None: No Basement\n\n"
            "- **BsmtFinSF1**: Type 1 finished square feet\n"
            "- **BsmtUnfSF**: Unfinished square feet of basement area\n"
            "- **GarageFinish**: Interior finish of the garage\n"
            "   - Fin: Finished;\n"
            "   - RFn: Rough Finished;\n"
            "   - Unf: Unfinished;\n"
            "   - None: No Garage\n"
            "- **KitchenQual**: Kitchen quality\n"
            "   - Ex: Excellent\n"
            "   - Gd: Good\n"
            "   - TA: Typical/Average\n"
            "   - Fa: Fair\n"
            "   - Po: Poor\n\n"
            "- **LotArea**: Lot size in square feet\n"
            "- **LotFrontage**: Linear feet of street connected to property\n"
            "- **MasVnrArea**: Masonry veneer area in square feet\n"
            "- **OpenPorchSF**: Open porch area in square feet\n"
            "- **OverallCond**: Rates the overall condition of the house\n"
            "   - 10: Very Excellent\n"
            "   - 9: Excellent\n"
            "   - 8: Very Good\n"
            "   - 7: Good\n"
            "   - 6: Above Average\n"
            "   - 5: Average\n"
            "   - 4: Below Average\n"
            "   - 3: Fair\n"
            "   - 2: Poor\n"
            "   - 1: Very Poor\n\n"
            "- **OverallQual**: Rates the overall material and finish of the house\n"
            "   - 1-10 same as OverallCond\n"
            "- **YearRemodAdd**: Remodel date (same as construction date if no remodeling or additions)\n\n"
            )
    st.write(
        f"To see dataset's source, please visit and **check** the "
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).")
    st.write("---")

    