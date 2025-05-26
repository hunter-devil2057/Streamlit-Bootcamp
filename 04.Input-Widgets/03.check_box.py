import streamlit as st
# st.checkbox(label, value(by default, False))

agree = st.checkbox("I agree")

if agree: 
    st.write("Great !!!")
    