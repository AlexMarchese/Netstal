import streamlit as st 
import pandas as pd
import numpy as np
import time
import random


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.sidebar.image("images/logo_netstal.webp", use_column_width=True)

# st.header("<h1>Status of Elion 1750</h1>")
st.markdown("<h1 style='text-align: center;'>Status of Elion 1750</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# Simulate position data
def get_deviation():
    deviation = random.uniform(-5, 5)
    return deviation
    # return np.random.normal(loc=75, scale=5)  # Random position data around 75 BPM

col1, col2 = st.columns([0.5, 0.5], gap="large", vertical_alignment="center")
video_file_1 = open("videos/view_1.mp4", "rb").read()
video_file_2 = open("videos/view_2.mp4", "rb").read()
# video_file_2 = video_file_1.copy()

with col1:


    # video_file_1 = open("videos/view_1.mp4", "rb").read()
    st.video(video_file_1, autoplay=True, loop=True, muted=True)

    

with col2:

    # video_file_2 = open("videos/view_1.mp4", "rb").read()
    st.video(video_file_2, autoplay=True, loop=True, muted=True)

# Page setup
st.subheader("Clamping mechanism")



# Placeholder for the real-time line chart
position_chart = st.empty()

# Initialize an empty DataFrame for position data
position_data = pd.DataFrame(columns=["Time", "Position"])

open = True

# Run the dynamic chart update loop
for i in range(100):  # Adjust the range for longer updates or use a while loop for indefinite updates
    # Get the current time and simulated position frequency
    current_time = pd.Timestamp.now().strftime("%H:%M:%S")
    if open:
        current_position = get_deviation() + 50
        open = False
    else:
        current_position = get_deviation() - 50
        open = True

    # Add new data to the DataFrame
    new_data = pd.DataFrame({"Time": [current_time], "Position": [current_position]})
    position_data = pd.concat([position_data, new_data]).tail(15)  # Show only the last 30 seconds of data
    
    # Update the chart with the new data
    position_chart.line_chart(position_data.set_index("Time"))

    # Pause for 1 second before getting the next data point
    time.sleep(1)

# Embedding a local video in a loop using HTML
# video_file = "videos/view_1.mp4"  # Replace with your local video file path
# video_file = "view_1.mp4"  # Replace with your local video file path

# video_html = f"""
#     <video width="700" height="400" controls autoplay loop muted>
#         <source src="{video_file}" type="video/mp4">
#         Your browser does not support the video tag.
#     </video>
#     """

# st.markdown(video_html, unsafe_allow_html=True)


# st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

