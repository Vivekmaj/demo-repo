import streamlit as st 
import joblib
import os
import numpy as np
import plotly.graph_objects as go
import sklearn


attrib_info = """
#### Attribute Information:
    - Age 1.20-65
    - Sex 1. Male, 2.Female
    - Polyuria 1.Yes, 2.No.
    - Polydipsia 1.Yes, 2.No.
    - Sudden weight loss 1.Yes, 2.No.
    - Weakness 1.Yes, 2.No.
    - Polyphagia 1.Yes, 2.No.
    - Genital thrush 1.Yes, 2.No.
    - Visual blurring 1.Yes, 2.No.
    - Itching 1.Yes, 2.No.
    - Irritability 1.Yes, 2.No.
    - Delayed healing 1.Yes, 2.No.
    - Partial paresis 1.Yes, 2.No.
    - Muscle stiffness 1.Yes, 2.No.
    - Alopecia 1.Yes, 2.No.
    - Obesity 1.Yes, 2.No.
    - Class 1.Positive, 2.Negative.

"""
label_dict = {"No":0,"Yes":1}
gender_map = {"Female":0,"Male":1}
target_label_map = {"Negative":0,"Positive":1}

['age', 'gender', 'polyuria', 'polydipsia', 'sudden_weight_loss',
       'weakness', 'polyphagia', 'genital_thrush', 'visual_blurring',
       'itching', 'irritability', 'delayed_healing', 'partial_paresis',
       'muscle_stiffness', 'alopecia', 'obesity', 'class']


def get_fvalue(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 



# Load ML Models
@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def run_ml_app():
	st.subheader("Machine Learning Section ⚙️")
	loaded_model = load_model("models/logistic_regression_model_diabetes_21_oct_2020.pkl")

	with st.expander("Attributes Info"):
		st.markdown(attrib_info,unsafe_allow_html=True)

	# Layout
	col1,col2 = st.columns(2)

	with col1:
		age = st.slider("Age",10,100)
		gender = st.radio("Gender",("Female","Male"))
		polyuria = st.radio("Polyuria",["No","Yes"])
		polydipsia = st.radio("Polydipsia",["No","Yes"]) 
		sudden_weight_loss = st.radio("Sudden_weight_loss",["No","Yes"])
		weakness = st.radio("weakness",["No","Yes"]) 
		polyphagia = st.radio("polyphagia",["No","Yes"]) 
		genital_thrush = st.radio("Genital_thrush",["No","Yes"]) 
		
	
	with col2:
		visual_blurring = st.radio("Visual_blurring",["No","Yes"])
		itching = st.radio("itching",["No","Yes"]) 
		irritability = st.radio("irritability",["No","Yes"]) 
		delayed_healing = st.radio("delayed_healing",["No","Yes"]) 
		partial_paresis = st.radio("Partial_paresis",["No","Yes"])
		muscle_stiffness = st.radio("muscle_stiffness",["No","Yes"]) 
		alopecia = st.radio("alopecia",["No","Yes"]) 
		obesity = st.radio("obesity",["No","Yes"]) 

	with st.expander("Your Selected Options"):
		result = {'age':age,
		'gender':gender,
		'polyuria':polyuria,
		'polydipsia':polydipsia,
		'sudden_weight_loss':sudden_weight_loss,
		'weakness':weakness,
		'polyphagia':polyphagia,
		'genital_thrush':genital_thrush,
		'visual_blurring':visual_blurring,
		'itching':itching,
		'irritability':irritability,
		'delayed_healing':delayed_healing,
		'partial_paresis':partial_paresis,
		'muscle_stiffness':muscle_stiffness,
		'alopecia':alopecia,
		'obesity':obesity}
		st.write(result)
		encoded_result = []
		for i in result.values():
			if type(i) == int:
				encoded_result.append(i)
			elif i in ["Female","Male"]:
				res = get_value(i,gender_map)
				encoded_result.append(res)
			else:
				encoded_result.append(get_fvalue(i))

	single_sample = np.array(encoded_result).reshape(1,-1)

	pred_prob = loaded_model.predict_proba(single_sample)

	prob = pred_prob[0][1] * 100
	thresh = 50
			
	fig = go.Figure(go.Indicator(
		mode = "gauge+number",
		value = prob,
		domain = {'x': [0, 1], 'y': [0, 1]},
		title = {'text': "Predicted Diabetes Probability (%)", 'font': {'size': 24}},
		gauge = {
				'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
				'bar': {'color': "red"},
				'bgcolor': "white",
				'borderwidth': 2,
				'bordercolor': "grey",
				'threshold': {
					'line': {'color': "orange", 'width': 4},
					'thickness': 0.75,
					'value': thresh}}))

	st.plotly_chart(fig)