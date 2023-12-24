import pandas as pd
import plotly.express as px
import requests
import streamlit as st 
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

selected_point = plotly_events(fig, click_event=True)

if len(selected_point) == 0:
	st.stop()

selected_x_value = selected_point[0]['x']
selected_y_value = selected_point[0]['y']
df_selected = df[(df['bill_length_mm']==selected_x_value) & (df['bill_depth_mm']==selected_y_value)]

st.write("Data for Selected Point:")
st.write(df_selected)
#st.plotly_chart(fig)






