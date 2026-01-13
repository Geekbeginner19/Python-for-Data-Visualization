# 🛠 MINI PROJECT 7 (YOU DO THIS)
# 🎯 Objective
# Practice time series visualization.

# 🧩 Task
# Create screen-time data for 10 days.

# Requirements
# ✔ Use pd.date_range()
# ✔ Create a DataFrame
# ✔ Use px.line()
# ✔ Add markers
# ✔ Use plotly_dark
# ✔ Proper axis labels
# ✔ Title included

# 💡 Example Theme Ideas
# Daily study hours
# Internet usage
# Fitness activity
# Screen time

import plotly.express as px 
import pandas as pd 

#creating a date range using pandas
dates = pd.date_range(start = "2025-01-12", periods = 10)
#Data
hours = [6, 8, 5, 3, 2, 3, 5, 7, 8, 6]

#creating a Dataframe with the data range
df = pd.DataFrame({
    "dates": dates, "hours": hours
})
#Plotting
#Pass dataframe columns instead of variables (Helps for better display of data when hovermode is applied)
figure = px.line(df, x = "dates", y = "hours", title = "Screen Time Data for the Last 10 Days")
#Styling
figure.update_layout(xaxis_title = "Date", yaxis_title = "Hours Spent", hovermode = "closest", template = "plotly_dark")
figure.update_traces(mode = "lines+markers")
figure.show()