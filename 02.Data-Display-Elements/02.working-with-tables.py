import numpy as np
import pandas as pd
import streamlit as st

# Generating Random Variable in DataFrame...
df = pd.DataFrame(
    np.random.randn(10, 5), 
    columns = ('col %d' %i for i in range(5))
)

# Displaying Table
st.table(df)