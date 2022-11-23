import numpy as np
import pandas as pd
import streamlit as st

class Classification():

    def __init__(self):
        # read data
        self.basic_data_old = pd.read_csv("./data/2020-08-19.csv").drop(['Unnamed: 0'], axis=1)
        # self.basic_data_new = pd.read_csv("./data/2022-01-08.csv").drop(['Unnamed: 0'], axis=1)
        # self.detailed_data = pd.read_csv("./data/games_detailed_info.csv")

        # self.review_data_1 = pd.read_csv("./data/bgg-15m-reviews.csv")
        # self.review_data_2 = pd.read_csv("./data/bgg-19m-reviews.csv")

    def filter_by_rate(self, df, min_rate=0, max_rate=10):
        result = df[(df['Average']>=min_rate) & (df['Average']<=max_rate)]
        
        return result

    def filter_by_year(self, df, min_year=0, max_year=2022):
        result = df[(df['Year']>=min_year) & (df['Year']<=max_year)]

        return result
