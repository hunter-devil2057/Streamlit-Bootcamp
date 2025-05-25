import numpy as np
import pandas as pd
import streamlit as st

# st.area_chart(data, x, y, height, width)

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns = ["X", "Y", "Z"]
)

st.area_chart(chart_data)