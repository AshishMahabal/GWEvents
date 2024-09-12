# app.py

import streamlit as st
from data_processing import load_data, filter_data
import matplotlib.pyplot as plt

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

# GraceDB (HierarchicalClass in event_predictions_table) Checkbox Filters
st.sidebar.subheader("GraceDB Object Types")
col1, col2, col3 = st.sidebar.columns(3)
glitch_gracedb = col1.checkbox("Glitch", value=False)
bbh_gracedb = col2.checkbox("BBH", value=True)
ns_gracedb = col3.checkbox("NS", value=True)
gracedb_types = [t for t, selected in zip(["Glitch", "BBH", "NS"], [glitch_gracedb, bbh_gracedb, ns_gracedb]) if selected]

# GWSkyNet (GDB_Class in event_predictions_table_metadata) Checkbox Filters
st.sidebar.subheader("GWSkyNet-Multi Object Types")
col4, col5, col6 = st.sidebar.columns(3)
glitch_gwskynet = col4.checkbox("Glitch", value=False, key="gwskynet_glitch")
bbh_gwskynet = col5.checkbox("BBH", value=True, key="gwskynet_bbh")
ns_gwskynet = col6.checkbox("NS", value=True, key="gwskynet_ns")
gwskynet_types = [t for t, selected in zip(["Glitch", "BBH", "NS"], [glitch_gwskynet, bbh_gwskynet, ns_gwskynet]) if selected]

# Significance Checkbox Filters
st.sidebar.subheader("Significance Levels")
col7, col8 = st.sidebar.columns(2)
high_significance = col7.checkbox("High", value=True)
low_significance = col8.checkbox("Low", value=False)
significance_levels = [s for s, selected in zip(["High", "Low"], [high_significance, low_significance]) if selected]

# Detectors Checkbox Filters
st.sidebar.subheader("Detectors")
col9, col10, col11 = st.sidebar.columns(3)
detector_h = col9.checkbox("H", value=True)
detector_l = col10.checkbox("L", value=True)
detector_v = col11.checkbox("V", value=False)
detector_choices = [d for d, selected in zip(["H", "L", "V"], [detector_h, detector_l, detector_v]) if selected]

# Filter Data
filtered_data = filter_data(data, gracedb_types, gwskynet_types, significance_levels, detector_choices)

# Dropdowns for selecting columns to plot
st.sidebar.subheader("Plot Settings")
x_axis_column = st.sidebar.selectbox("Select X-axis column", options=filtered_data.columns, index=2)
y_axis_column = st.sidebar.selectbox("Select Y-axis column", options=filtered_data.columns, index=3)

# Main content
st.title("Filtering Gravitational Wave Alerts")
st.write("Use the sidebar to filter GW alerts based on different options.")

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))

for idx, row in filtered_data.iterrows():
    # Determine symbol and size
    if row['HierarchicalClass'] == "Glitch":
        marker = 'x'  # Cross for glitches
    elif row['HierarchicalClass'] == "BBH":
        marker = 'o'  # Circle for BBH
    elif row['HierarchicalClass'] == "NS":
        marker = 's'  # Square for NS
    else:
        marker = 'o'  # Default to circle if something unexpected

    size = 100 if row['Significant'] else 30  # Bigger size for significant events

    # Determine color: Green if GraceDB and GW SkyNet classes are the same, otherwise default color
    color = 'green' if row['HierarchicalClass'] == row['GDB_Class'] else 'blue'

    # Plot each point
    ax.scatter(row[x_axis_column], row[y_axis_column], s=size, c=color, marker=marker, label=row['EventName'])

# Add labels and title
ax.set_xlabel(x_axis_column)
ax.set_ylabel(y_axis_column)
ax.set_title("Scatter Plot of Gravitational Wave Alerts")

st.pyplot(fig)

# Display filtered data
st.write(filtered_data)
st.write("Number of filtered rows: ", len(filtered_data))