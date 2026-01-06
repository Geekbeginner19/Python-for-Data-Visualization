# 📊 Stackplot Project 1: Monthly Expense Breakdown
# 🎯 Goal

# Show how different expense categories contribute to total monthly spending.

# 📁 Data Example
# 6–8 months
# Rent: [500, 500, 500, 500, 500, 500]
# Food: [150, 160, 170, 165, 180, 190]
# Transport: [60, 70, 65, 75, 80, 85]
# Entertainment: [40, 50, 45, 55, 60, 65]

# 🔍 Insight
# Which expense dominates?
# How total spending trends over time

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Rent = [300, 400, 600, 700, 800, 950]
Food = [130, 145, 130, 150, 125, 185]
Transport = [60, 65, 90, 75, 45, 50]
Entertainment = [40, 20, 40, 10, 30, 80]

font1 = {"family": "verdana", "color" : "red", "size" : 20}
font2 = {"family": "serif", "color" : "green", "size" : 15}

labels = ["Rent", "Food", "Transport", "Entertainment"]
plt.grid(color = "k", linestyle = ":")
plt.stackplot(months, Rent, Food, Transport, Entertainment, labels = labels)
plt.title("Monthly Expense Breakdown", fontdict = font1)
plt.xlabel("Months", fontdict = font2)
plt.ylabel("Expenses", fontdict = font2)
plt.legend(loc = "lower left", title = "Expenses")
plt.show()
