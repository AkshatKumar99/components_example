import pandas as pd
import plotly.express as px
import requests
import streamlit as st 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_lottie import st_lottie 
from streamlit_plotly_events import plotly_events 

def load_lottieurl(url: str):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

lottie_animation = load_lottieurl('https://lottie.host/aef5b04e-e4b1-410b-a462-b496ff2cffea/d8SAdmKw2c.json')
st_lottie(lottie_animation, height=200, speed=0.5)

st.title('Streamlit Plotly Events + Lottie Example: Penguins')
df = pd.read_csv('penguins.csv')

fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species')

st.subheader('Pandas Profiling of Penguin Dataset')
penguin_profile = ProfileReport(df, explorative=True)

st_profile_report(penguin_profile)

