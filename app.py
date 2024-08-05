import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('census_2011_cleaned.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'India')

st.sidebar.title('India Census 2011 Analysis')

selected_state = st.sidebar.selectbox('Select State', list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter', list(df.columns[4:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', list(df.columns[4:]))

plot = st.sidebar.button('Analyze')
