# app.py

import streamlit as st
from data_processing import load_data, filter_data

# Set page configuration
st.set_page_config(
    page_title="Gravitational Wave Alert Filtering",
    layout="wide"
)

# Load data
#@st.cache_data
def load_merged_data():
    return load_data('GraceDB.csv', 'GWSkyNet.csv')

data = load_merged_data()
#st.write(data)

# Sidebar - Checkbox filters
st.sidebar.header("Filter Options")

# GraceDB Checkbox Filters
gracedb_types = st.sidebar.multiselect(
    "GraceDB Object Types",
    options=["Glitch", "BBH", "NS"],
    default=["BBH", "NS"]
)

# GWSkyNet Checkbox Filters
gwskynet_types = st.sidebar.multiselect(
    "GWSkyNet-Multi Object Types",
    options=["Glitch", "BBH", "NS"],
    default=["BBH", "NS"]
)

# Significance Checkbox Filters
significance_levels = st.sidebar.multiselect(
    "Significant Events",
    options=["High", "Low"],
    default=["High"]
)

# Filter Data
filtered_data = filter_data(data, gracedb_types, gwskynet_types, significance_levels)

# Main content
st.title("Gravitational Wave Astronomy Alert Filtering")
st.write("Use the options in the sidebar to filter gravitational wave alerts based on different object types and significance levels.")

# Display filtered data
st.write(filtered_data)
