import streamlit as st

def hypothesis_page_body():   

    st.write("### Project Hypothesis and Validation :pencil:")
    st.success(    
        f"**Hypothesis 1:** We suspect properties with greater Overall Quality will be priced higher.\n\n"
        f"* **Hypothesis validation:** The first hypothesis argument is supported by the fact of correlation analysis that homes with greater Overall Quality typically have higher sale prices.\n\n"
        f"**Hypothesis 2:** We suspect properties with larger spaces will be priced higher.\n\n"
        f"* **Hypothesis validation:** The correlation study between SalePrice and space variables supports this.\n\n"
        f"**Hypothesis 3:** We suspect the more recent the year of construction, the higher the sale price tends to be.\n\n"
        f"* **Hypothesis validation:** The correlation study between SalePrice and YearBuilt supports this.\n\n"
        
    )



    