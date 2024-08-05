import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('census_2011_cleaned.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'India')

st.sidebar.title('India Census 2011 Analysis')

selected_state = st.sidebar.selectbox('Select State', list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter', list(df.columns[4:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', list(df.columns[4:]))

plot = st.sidebar.button('Analyze')

if plot:
    if selected_state == 'India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=3.5, size_max=35, mapbox_style='carto-positron', width=1080, height=700)
        st.plotly_chart(fig, use_container_width=True)
    else:
        pass