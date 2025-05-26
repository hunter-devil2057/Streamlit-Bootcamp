import streamlit as st
import datetime

date = st.date_input(
    "When is you Birthday? ", 
    # Default value of date
    datetime.date(2019, 7, 6))

st.write("Your Birthday is: ", date)