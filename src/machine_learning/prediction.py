import streamlit as st

def predict_sale_price(X_live, sale_price_features, sale_price_pipeline):

	X_live_sale_price = X_live.filter(sale_price_features)


	sale_price_prediction_proba = sale_price_pipeline.predict(X_live_sale_price)

	proba = sale_price_prediction_proba
	value = float(proba.round(1))
	amount = '${:,.2f}'.format(value)
	statement = (
		f'The House Sale Price Estimation: **{amount}**'
		)

	st.write(statement)