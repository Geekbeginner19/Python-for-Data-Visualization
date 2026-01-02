# Monthly Expense Breakdown (Pie Chart)
# 🎯 Goal

# Practice:
# Pie charts
# Custom colors
# Edge colors
# Percentages on slices

# 🧠 Scenario
# You are visualizing how your monthly income is spent.

import matplotlib.pyplot as plt

font1 = {"family" : "serif", "color" : "black", "size" : 15}
font2 = {"family" : "verdana", "color" : "darkred", "size" : 12}

expenses = [500, 300, 200, 150, 100]
categories = ["Rent", "Food", "Transport", "Utilities", "Entertainment"]
colors = ["red", "brown", "cyan", "magenta", "blue"]

plt.title("Monthly Expense Breakdown", fontdict = font1) #You don't need an x and y axis for the Pie Chart
wedgeprops = {"linewidth" : 2, "edgecolor" : "white"}
plt.axis("equal") # Enforces Perfect circular shape (Without this, pies may appear slightly oval on some screens)

plt.pie(expenses, labels = categories, wedgeprops = wedgeprops, autopct = "%1.1f%%", colors = colors)
plt.legend(title = "Expense Categories", loc = "lower left")
plt.show()

