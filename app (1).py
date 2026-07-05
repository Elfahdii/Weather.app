import streamlit as st
import pandas as pd


df = pd.read_csv('salaryy(1).csv')
print(df.head())
print("Done")
st.write(df)
