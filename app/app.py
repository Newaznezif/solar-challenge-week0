import streamlit as st
import pandas as pd

st.title("☀️ Solar Challenge Dashboard")
st.write("Welcome to the Solar Energy Analytics Dashboard!")

data = pd.DataFrame({
    "Location": ["Addis Ababa", "Gondar", "Adama"],
    "Solar Output (kWh)": [120, 95, 130]
})
st.bar_chart(data.set_index("Location"))
