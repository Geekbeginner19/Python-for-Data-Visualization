# 🛠 MINI PROJECT 2
# 🎯 Objective
# Practice plotting from Pandas.

# 🧩 Task
# Create a DataFrame showing your weekly expenses.

# Example columns:
# Day
# Amount_Spent

# Requirements
# ✔ Use Pandas
# ✔ Use plotly.express
# ✔ Use a bar chart
# ✔ Add a title

import plotly.express as px #For plotting information
import pandas as pd #For processing data
import cufflinks as cf #Cufflinks is really old and poorly maintained by DEVs so it's not reliable at all
cf.go_offline() #Makes no difference when omitted

#Creating a DataFrame to process the original data (Original Data HAS to be converted to a dictionary)
df = pd.DataFrame({'Days' : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
'Hours_spent' : [5, 7, 3, 8, 5, 1, 6]
})
#Plotting the data
figure = px.line(df, x = 'Days', y = 'Hours_spent', title = 'Weekly Phone Usage (Using Pandas)', color_discrete_sequence = ["lightblue"], template = "plotly_dark")

#Adding Markers to Lines (Plotly expects NO SPACES in the mode string) 
figure.update_traces(mode = "lines+markers")

#Labelling Axes & Changing Figure Size
figure.update_layout(xaxis_title = "Days of the Week", yaxis_title = "Hours Spent on Phone", width = 900, height = 450)

#Displaying the graph
figure.show()
