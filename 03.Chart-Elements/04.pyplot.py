import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

arr = np.random.normal(1, 1, size =100)
fig, axis = plt.subplots()
axis.hist(arr, bins = 20)
st.pyplot(fig)