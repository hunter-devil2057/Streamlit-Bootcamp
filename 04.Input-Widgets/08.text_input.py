import streamlit as st

title = st.text_input("Movie Title", 
                    # By Default, Life of Brian is shown. 
                      "Life of Brian")

st.write("The current movie title is: ", title)