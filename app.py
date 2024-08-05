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
    st.text('Size represent Primary parameter.')
    st.text('Color represent Secondary parameter.')
    if selected_state == 'India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=3.5, size_max=35, mapbox_style='carto-positron', width=1080, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=5, size_max=35, mapbox_style='carto-positron', width=1080, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)