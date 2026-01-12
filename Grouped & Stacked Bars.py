# 🛠 MINI PROJECT 6 (IMPORTANT)
# 🎯 Objective
# Practice grouped & stacked bars.

# 🧩 Task
# Create a dataset comparing two or three categories across days or types.

# Examples:
# Food vs Transport expenses per day
# Morning vs Evening activity
# Weekday vs Weekend screen time

# Requirements
# ✔ Use Pandas
# ✔ Use Plotly Express
# ✔ Create ONE grouped bar chart
# ✔ Create ONE stacked bar chart
# ✔ Add titles and axis labels
# ✔ Use plotly_dark

import plotly.express as px
import pandas as pd 

#Using Pandas to create the DataFrame for plotting 
df = pd.DataFrame({
    'Day': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] * 2,
    'Expense': ['Food'] * 7 + ['Transportation'] * 7,
    'Amount': [50, 70, 30, 35, 55, 25, 40, 45, 39, 40, 60, 80, 25, 10]
})

#Figure for a Grouped Bar Chart
figure = px.bar(df, x = "Day", y = "Amount", color = "Expense", title = "Food vs Transport Expenses Per Day (Grouped)", barmode = "group")
figure.update_layout(xaxis_title = "Day", yaxis_title = "Amount", template = "plotly_dark", hovermode = "closest")

#Figure for a Stacked Bar Chart
figure_stacked = px.bar(
    df,
    x="Day",
    y="Amount",
    color="Expense",
    title="Food vs Transport Expenses Per Day (Stacked)",
    barmode="stack"
)

figure_stacked.update_layout(
    xaxis_title="Day",
    yaxis_title="Amount",
    template="plotly_dark",
    hovermode="closest"
)

figure.show()
figure_stacked.show()