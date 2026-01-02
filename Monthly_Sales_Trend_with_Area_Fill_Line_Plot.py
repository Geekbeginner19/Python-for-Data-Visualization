# Monthly Sales Trend with Area Fill (Line Plot)
# 🎯 Goal
# Practice:
# Color fill (fill_between)
# Adding titles to legends
# Clean, readable line plotting

# 🧠 Scenario
# You are analyzing monthly sales for two products in a small business.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_A = [1200, 1500, 1700, 1600, 1800, 2000]
product_B = [1000, 1100, 1300, 1400, 1500, 1700]
font1 = {"family" : "serif", "color" : "blue", "size" : 15}
font2 = {"family" : "verdana", "color" : "green", "size" : 12}

plt.title("Monthly Sales Trend", fontdict = font1)
plt.xlabel("Months", fontdict = font2)
plt.ylabel("Products Sales", fontdict = font2)

plt.style.use("seaborn-v0_8") #Styles should be set before plotting
plt.plot(months, product_A, color = "r", linestyle = "-", marker = "o", label = "Product A")
plt.plot(months, product_B, color = "b", linestyle = ":", marker = "s", label = "Product B")

plt.legend(title = "Products")#Adding titles to legend
plt.grid()

#Filling between the lines 
plt.fill_between(months, product_B, alpha = 0.5, color = "b")
plt.fill_between(months, product_A, alpha = 0.3, color = "r")
plt.show()




