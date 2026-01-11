# MINI PROJECT 1 (VERY IMPORTANT)
# 🎯 Objective
# Practice exactly what you just learned.

# 🧩 Task
# Create a line chart that shows your weekly phone usage hours.

# Rules:
# Use lists
# Use plotly.express
# Add a title
# Use .show()

# Example idea (don’t copy blindly):
# Days: Monday → Sunday
# Hours: Any realistic numbers

import plotly.express as px 

#Data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_spent = [5, 7, 3, 8, 5, 1, 6]

#Plotting the data using plotly
figure = px.line(x = days, y = hours_spent, title = "Weekly Phone Usage Hours")

figure.show()