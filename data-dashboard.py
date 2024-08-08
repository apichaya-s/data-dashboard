import streamlit as st
import pandas as pd

st.title("Tips Dashboard with streamlit")
tips_df = pd.read_csv("tips.csv")

st.dataframe(tips_df)
