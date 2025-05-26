import streamlit as st

# st.radio(label, options, index)

genre = st.radio(
    "What's your Favourite Movie Genre", 
    ("Comedy", "Drama", "Documentary")
)

if genre == "Comedy":
    st.write("You selected Comedy.")
else:
    st.write("You didn't select Comedy.")