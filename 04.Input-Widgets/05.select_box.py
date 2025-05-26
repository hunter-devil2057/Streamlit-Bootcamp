import streamlit as st

# st.selectbox(label, (options), index)
option = st.selectbox(
    "How would you like to be contacted?", 
    ("Email", "Home Phone", "Mobile Phone")
)

st.write(f"You Selected: {option}")