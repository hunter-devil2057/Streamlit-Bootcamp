import streamlit as st

# Writing Title
st.title("I am Title")

# Writing Header
st.header("I am Header")

# Writing Sub-Header
st.subheader("I am Sub-Header")

# Writing MarkDown
st.markdown("I am Markdown")

# Adding Code Block
st.code("I am code block. \nEg:\nint a = 5")

# Writing out Text
st.text("I am Text")

# Write: Is like: Swiss Army Knife that accepts multiple arguments and multiple data-types 
st.write("I am write.")



# Note: For Executing the Code, please do, streamlit run <fileName>



var1 = "Hello, user"

var2 = 5

st.write("Value of var1: ", var1)
st.write("Value of var2: ", var2)