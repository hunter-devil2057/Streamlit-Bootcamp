import numpy as np
import pandas as pd
import streamlit as st

# Defining DataFrame
# st.dataframe(data = source, width and height)

st.write("This is a DataFrame Demo...")

df = pd.DataFrame(
    np.random.randn(50, 20), 
    columns = ('col %d' %i for i in range(20)) 
)

st.dataframe(df, height = 900, width = 1000)