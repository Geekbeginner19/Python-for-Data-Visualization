# 🛠 MINI PROJECT 5
# 🎯 Objective
# Practice comparative visualization.

# 🧩 Task
# Create data for:
# At least 2 categories
# Across days or time

# Examples:
# Phone vs Laptop usage
# Morning vs Evening activity
# Weekday vs Weekend spending

# Requirements
# ✔ Use Pandas
# ✔ Use Plotly Express
# ✔ Multi-line or grouped chart
# ✔ Add title
# ✔ Use color for categories

import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Day': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] * 2,
    'Device': ['Phone'] * 7 + ['Tablet'] * 7,
    'Hours': [5, 7, 3, 8, 5, 1, 6, 2, 3, 4, 6, 5, 2, 1]
})

fig = px.line(
    df,#indicating the data to use for plotting
    x='Day',
    y='Hours',
    color='Device',#Categorising the colors to Device Types
    title='Weekly Usage: Phone vs Tablet',
    markers=True
)
fig.update_layout(xaxis_title = "Days", yaxis_title = "Number of Hours of Usage", template = "plotly_dark")

fig.show()
