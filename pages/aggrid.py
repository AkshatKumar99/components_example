import pandas as pd 
import streamlit as st
from st_aggrid import AgGrid

st.set_page_config(layout='wide')

st.title("Streamlit AgGrid Example: Penguins")
penguins_df = pd.read_csv('penguins.csv')

st.write('AgGrid DataFrame:')
response = AgGrid(penguins_df, height=500, editable=True, enable_quicksearch=True, theme='streamlit')

df_edited = response['data']
st.write("Edited DataFrame:")
st.dataframe(df_edited)

