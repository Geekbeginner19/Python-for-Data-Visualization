# 🛠 MINI PROJECT 8
# 🎯 Objective
# Learn how to combine multiple charts into one figure using subplots.

# 🧩 TASK
# Create ONE figure with TWO subplots:

# Plot 1 (Top)
# 📈 Line chart
# Daily Screen Time (hours)

# Plot 2 (Bottom)
# 📊 Bar chart
# Daily App Usage Count

# 📋 REQUIREMENTS
# ✔ Use Pandas
# ✔ Use plotly.subplots.make_subplots
# ✔ Two rows, one column
# ✔ Shared X-axis
# ✔ Add titles for each subplot
# ✔ Use plotly_dark
# ✔ Proper axis labels

from plotly.subplots import make_subplots 
import plotly.graph_objects as go 
import pandas as pd 

#Creating a data range using pandas
date = pd.date_range(start = "2025-01-12", periods = 7)
#Data for Screen time Usage
screen_time = [3, 5, 8, 2, 1, 4, 7]
#Data for App usage count
app_use = [5, 9, 4, 6, 8, 2, 4]

df = pd.DataFrame(
    {
        "date":date,
        "screen_time":screen_time,
        "App_Usage": app_use
    }
)

fig = make_subplots(rows = 2, cols = 1, shared_xaxes = True, subplot_titles=("Screen Time", "Daily App Usage"))

fig.add_trace(go.Scatter(
    x = df["date"],
    y = df["screen_time"],
    mode = "lines+markers",
    name = "Screen Time (Hours)"
), row = 1, col = 1 
)

fig.add_trace(
    go.Bar(
        x = df["date"],
        y = df["App_Usage"],
        name = "App Usage"
    ),
    row = 2, col = 1
)

# ✅ AXIS LABELS GO HERE
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Screen Time (Hours)",
    xaxis2_title="Date",
    yaxis2_title="App Usage Count",
    template="plotly_dark",
    hovermode = "x unified"
)

fig.show()