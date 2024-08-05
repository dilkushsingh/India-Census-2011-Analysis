import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('census_2011_cleaned.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'India')

st.sidebar.title('India Census 2011 Analysis')

st.sidebar.selectbox('Select State', list_of_states)
