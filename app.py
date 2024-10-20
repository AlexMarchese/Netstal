import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Sample machine data
machines = [
    {"id": 1, "name": "Pump A", "status": "Active", "temperature": 72, "vibration": 0.03},
    {"id": 2, "name": "Pump B", "status": "Critical", "temperature": 95, "vibration": 0.12},
    {"id": 3, "name": "Pump C", "status": "Normal", "temperature": 80, "vibration": 0.05},
]

# Function to generate prediction data
def generate_prediction_data():
    today = datetime.now()
    return [
            {
            "date": (today + timedelta(days=i)).strftime("%Y-%m-%d"),
            "failure_chance": random.uniform(0.1, 0.9)
        } for i in range(7)
    ]

# Sidebar for navigation
st.sidebar.image("images/logo_netstal.webp", use_column_width=True)
# st.sidebar.title("Navigation")
# page = st.sidebar.selectbox("Go to", ["Dashboard", "Machines", "Components", "Models"])


# st.page_link("app.py", label="Home", icon="🏠")
# st.page_link("pages/machines.py", label="Page 1", icon="1️⃣")
# st.page_link("pages/components.py", label="Page 2", icon="2️⃣", disabled=True)
# st.page_link("http://www.google.com", label="Google", icon="🌎")






# Mocked machine statuses
machine_statuses = [
    {"name": "Pump A", "status": "Critical", "error_rate": 52},
    {"name": "Pump B", "status": "Critical", "error_rate": 46},
    {"name": "Pump C", "status": "Normal", "error_rate": 100},
]


# # Sample data for the pie chart
# labels = ['Category A', 'Category B', 'Category C', 'Category D']
# values = [4500, 2500, 1050, 1500]

# # Create a donut chart using Plotly
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])

# # Add a title to the chart
# fig.update_layout(title_text="Donut Chart Example")

# # Display the chart in the Streamlit app
# st.plotly_chart(fig)

# Create two columns: left for the chart, right for other content
col1, col2 = st.columns([1, 2])

with col1:
    # Sample data for the pie chart
    labels = ['ELH 4200 I', 'ELH 4200 II', 'ELE 1750 I', 'ELE 1750 II']
    values = [4500, 2500, 1050, 1500]

    # Create a donut chart using Plotly
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])

    # Add a title to the chart
    fig.update_layout(title_text="Running time")

    # Display the chart in the Streamlit app
    st.plotly_chart(fig, use_container_width=True)

with col2:


    st.subheader("Most Critical States")

    # Display machine status and error rates with warning icons
    for machine in machine_statuses:
        if machine['status'] == 'Critical':
            st.markdown(f"🟠 **{machine['name']}** - {machine['error_rate']}% error rate")
        else:
            st.markdown(f"🟢 **{machine['name']}** - {machine['error_rate']}% error rate")

   


 # # Display machine information
st.subheader("Machines Overview")

# Sample data for the line charts
data = {
    "time": [datetime.now() - timedelta(hours=i) for i in range(24)],
    "Pump A": [random.uniform(-0.5, 0.5) for _ in range(24)],
    "Pump B": [random.uniform(-0.5, 0.5) for _ in range(24)],
    "Pump C": [random.uniform(-0.5, 0.5) for _ in range(24)],
}

df = pd.DataFrame(data)
df['time'] = pd.to_datetime(df['time'])

# Create a figure for the line charts using Plotly
fig = go.Figure()

# Adding traces for each pump (similar to the example chart in the image)
fig.add_trace(go.Scatter(x=df['time'], y=df['Pump A'], mode='lines', name='Pump A', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=df['time'], y=df['Pump B'], mode='lines', name='Pump B', line=dict(color='orange')))
fig.add_trace(go.Scatter(x=df['time'], y=df['Pump C'], mode='lines', name='Pump C', line=dict(color='green')))

# Customizing the layout to be similar to the provided image
fig.update_layout(
    title="Pump Monitoring (Past 24 Hours)",
    xaxis_title="Time",
    yaxis_title="Exerted pressure (in % of avg)",
    legend_title="Pumps",
    xaxis=dict(tickformat='%H:%M'),  # Format to show only hours and minutes
    height=400,
    margin=dict(l=40, r=40, t=50, b=40)
)

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)
# machine_df = pd.DataFrame(machines)
# st.dataframe(machine_df)

# # Predicted failure chart
# st.subheader("Failure Predictions")
# prediction_data = generate_prediction_data()
# prediction_df = pd.DataFrame(prediction_data)
# st.line_chart(prediction_df.set_index('date'), height=250)
# st.write(prediction_df)


# # Dashboard Page
# if page == "Dashboard":
#     st.title("Dashboard Overview")
    
#     # Overview of Machine Statuses
#     st.subheader("Overall Machine States")
#     machine_df = pd.DataFrame(machines)
#     st.dataframe(machine_df)

#     # Predicted failure chart
#     st.subheader("Failure Predictions")
#     prediction_data = generate_prediction_data()
#     prediction_df = pd.DataFrame(prediction_data)
#     st.line_chart(prediction_df.set_index('date'), height=250)
#     st.write(prediction_df)

# # Machines Page
# elif page == "Machines":
#     st.title("Machines Monitoring")
    
#     # Display machine information
#     st.subheader("Machines Overview")
#     for machine in machines:
#         st.write(f"Machine: {machine['name']}")
#         st.write(f"Status: {machine['status']}")
#         st.write(f"Temperature: {machine['temperature']}°F")
#         st.write(f"Vibration: {machine['vibration']}g")
#         st.write("---")

# # Components Page
# elif page == "Components":
#     st.title("Components Details")
    
#     # Placeholder for components information (example)
#     components = [{"name": "Valve A", "status": "Operational"}, {"name": "Valve B", "status": "Maintenance Needed"}]
#     st.subheader("Component Status")
#     for component in components:
#         st.write(f"Component: {component['name']} | Status: {component['status']}")
#         st.write("---")

# # Models Page
# elif page == "Models":
#     st.title("Machine Learning Models")
    
#     # Example content for the models page
#     st.subheader("Predictive Models in Use")
#     models = ["Anomaly Detection Model v1.2", "Failure Prediction Model v2.5", "Temperature Sensor Model v1.1"]
#     for model in models:
#         st.write(f"Model: {model}")
