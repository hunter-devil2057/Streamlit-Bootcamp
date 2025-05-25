import numpy as np
import pandas as pd
import streamlit as st

# st.bar_chart(data, x, y, width, height)

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns = ["a", "b", "c"]
)

st.bar_chart(chart_data)