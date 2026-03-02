import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Simple Demo App", layout="centered")

# Title
st.title("🚀 Simple Streamlit App")

st.write("This is a basic interactive demo application.")

# Sidebar
st.sidebar.header("Settings")

multiplier = st.sidebar.slider("Select Multiplier", 1, 10, 2)
number = st.sidebar.number_input("Enter a number", value=5)

# Main Section
st.header("Calculation")

result = number * multiplier

st.success(f"Result: {result}")



st.write("App created successfully 🎉")