import streamlit as st
from datetime import time 
from datetime import datetime

age = st.slider(
    "How old are you?", 
    0, 130, 25
)

st.write("I am ", age, " years old.")

values = st.slider(
    "Select a Range of Values: ", 
    0.0, 100.0, (25.0, 75.0)
)

st.write("Values: ", values)

appointment = st.slider(
    "Schedule your appointment", 
    value = (time (11, 30), time(12, 45))
)
st.write("Appointment Date: ", appointment)

start_time = st.slider(
    "When do you start?", 
    value = (datetime(2020, 1, 1, 9, 30)), 
    format = "MM/DD/YY - hh:mm"
)

st.write("Start Time: ", start_time)