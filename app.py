import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from ml_app import run_ml_app

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


html_temp = """
		<div style="background-color:tomato;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Diabetes Risk Data App </h1>
		</div>
		"""

def main():

	# st.title("ML Web App with Streamlit")
	stc.html(html_temp)

	menu = ["Home","EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			### Early Stage Diabetes Risk Predictor App 💉
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			The dataset can be found [here](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.).
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: Machine Learning Predictor App

			""")
	elif choice == "EDA":
		run_eda_app()
	elif choice == "ML":
		run_ml_app()
	else:
		st.subheader("About")

if __name__ == '__main__':
	main()