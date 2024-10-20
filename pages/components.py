import streamlit as st
import pandas as pd


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.sidebar.image("images/logo_netstal.webp", use_column_width=True)

# Sensor-based predictions components
sensor_based_components = [
    {"name": "Druckaufnehmer (Pressure sensor)", "usage": "78%"},
    {"name": "Hydraulikzylinder (Hydraulic cylinder)", "usage": "65%"},
    {"name": "Umrichter (Converter)", "usage": "85%"},
    {"name": "Injection unit displacement cylinderhead", "usage": "60%"},
    {"name": "Akkumulator (Accumulator)", "usage": "70%"}
]

# Time-based predictions components
time_based_components = [
    {"name": "Proportional-Wegeventil (Proportional valve)", "usage": "70%"},
    {"name": "Wegeventil (Valve)", "usage": "55%"},
    {"name": "IPC-Modul (Control module)", "usage": "90%"},
    {"name": "Heizung (Heating unit)", "usage": "60%"},
    {"name": "Filterelement (Filter)", "usage": "50%"},
    {"name": "Steuerkabel GS (Control cable)", "usage": "65%"}
]

# Create Streamlit page
st.title("Components Page")
st.write("This page lists components and their level of usage, predicting when they need to be replaced.")

# Sensor-based components section
st.subheader("Sensor-based Predictions")
st.write("For these components, we monitor their level of usage through sensor data and predict when they need to be replaced.")
sensor_df = pd.DataFrame(sensor_based_components)
st.table(sensor_df)

# Time-based components section
st.subheader("Time-based Predictions")
st.write("For these components, we predict replacements based on operational time or maintenance schedules.")
time_df = pd.DataFrame(time_based_components)
st.table(time_df)
