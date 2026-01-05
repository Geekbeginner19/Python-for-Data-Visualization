# 📊 PROJECT 2 — Sales Performance Comparison
# (Overlaying Bar Plots)

# 🎯 Goal
# Practice:
# Overlaying bar charts
# Alignment and spacing
# Comparative visual analysis

# 🧠 Scenario
# You are comparing monthly sales of two competing products in the same store.

# 📁 Data
# 6–8 months
# Sales for Product A
# Sales for Product B

import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

#You need to use NUMPY Arrays to make the stacks possible
product_A = np.array([1200, 1300, 1450, 1500, 1600, 1700, 1750, 1800])
product_B = np.array([1100, 1250, 1400, 1420, 1500, 1550, 1600, 1650])
product_C = np.array([900, 1000, 1100, 1200, 1250, 1300, 1350, 1400])
product_D = np.array([1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850])
product_E = np.array([800, 900, 950, 1000, 1050, 1100, 1150, 1200])

font1 = {"family": "courier new", "color" : "red", "size" : 22}
font2 = {"family": "serif", "color" : "green", "size" : 17}

plt.bar(months, product_A, color = "r", label = "Product A")
plt.bar(months, product_B, bottom = product_A, color = "b", label = "Product B")
plt.bar(months, product_C, bottom = product_A + product_B, color = "y", label = "Product C")
plt.bar(months, product_D, bottom = product_A + product_B + product_C, color = "g", label = "Product D")
plt.bar(months, product_E, bottom = product_A + product_B + product_C + product_D, color = "pink", label = "Product E")
plt.legend(title = "Product Sales")
plt.title("Sales Performance Comparison", fontdict = font1)
plt.xlabel("Months", fontdict = font2)
plt.ylabel("Number of Sales", fontdict = font2)
plt.show()
