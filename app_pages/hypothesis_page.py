import streamlit as st

def hypothesis_page_body():

    st.write("Welcome to the *Heritage House Project!* :house:")

    st.write(
            "- **YearBuilt**: Original construction date\n"
            "- **TotalBsmtSF**: Total square feet of basement area\n"
            "- **GrLivArea**: Above grade (ground) living area square feet\n"
            "- **OverallQual**: Rates the overall material and finish of the house\n"
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
            "- **KitchenQual**: Kitchen quality\n"
            "   - Ex: Excellent\n"
            "   - Gd: Good\n"
            "   - TA: Typical/Average\n"
            "   - Fa: Fair\n"
            "   - Po: Poor\n\n"
        )
    