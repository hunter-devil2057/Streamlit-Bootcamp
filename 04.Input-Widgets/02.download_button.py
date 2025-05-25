import pandas as pd
import streamlit as st

sample_text = "Some Text that will be downloaded..."
st.download_button("Download Text", sample_text)
# st.download_button("Button Text", text_to_download)

with open("gratisography-augmented-reality.jpg", "rb") as file:
    btn = st.download_button(
        label = "Download Image", 
        data = file, 
        file_name = "gratisography-augmented-reality.jpg", 
        mime = "image/jpg"
    )

# Makes faster for Larger File Size
@st.cache_data

def convert_df(df):
    return df.to_csv().encode('utf-8')

df1 = pd.read_csv("addresses.csv")
csv = convert_df(df1)

st.download_button(
    label = "Download data as csv", 
    data = csv, 
    file_name = "large_df.csv", 
    mime = "text/csv"
)