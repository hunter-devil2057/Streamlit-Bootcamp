import streamlit as st

# using: st.button(label, onclick, key(optional integer or string))

if st.button("Say Hello"):
    st.write("Hey, Hello There!")
else:
    st.write("Good Byee...")