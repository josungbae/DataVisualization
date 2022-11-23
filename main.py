import numpy as np
import pandas as pd
import streamlit as st
import requests
from io import BytesIO
from PIL import Image

from classification import Classification
# from network import Network


task = st.sidebar.selectbox(
    "What do you want to see?",
    ("Classification", "Network")
)

if task == "Classification":
    st.title("Boardgames - Classification")
    cf = Classification()

    # set a range of the average rate for the games to display
    rate_range = st.slider(label='Set a range of the average rate', 
                    min_value=0.0,
                    max_value=10.0,
                    value=(0.0, 10.0), # initial setting
                    label_visibility='visible'
                    )
    min_rate, max_rate = rate_range

    # set a range of the year for the games to display
    year_range = st.slider(label='Set a range of the year', 
                    min_value=0,
                    max_value=2022,
                    value=(0, 2022), # initial setting
                    label_visibility='visible'
                    )
    min_year, max_year = year_range

    # filtering & display the dataframe
    filtered_df = cf.filter_by_rate(cf.basic_data_old, min_rate, max_rate)
    filtered_df = cf.filter_by_year(filtered_df, min_year, max_year)
    filtered_df = filtered_df.drop(['ID'],axis=1)
    filtered_df = filtered_df.set_index(['Name'])

    st.write(filtered_df)

elif task == "Network":
    st.title("Boardgames - Network")
