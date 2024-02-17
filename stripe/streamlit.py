import pandas as pd
import streamlit as st

# Add a title
st.title('Streamlit Tutorials')

# pull data from seeds_db/merged.csv
merged = pd.read_csv('data/seeds_db/merged.csv')
valid = pd.read_csv('data/valid_cc.csv')

# display merged dataframe on the UI
st.write(valid)