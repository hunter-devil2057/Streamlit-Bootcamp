import numpy as np
import pandas as pd
import streamlit as st

# st.line_chart(data, x, y, width, height)

chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns = ["A", "B", "C"]
)

st.line_chart(chart_data)