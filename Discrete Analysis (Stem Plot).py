# 🟥 FIGURE 3 — DISCRETE ANALYSIS
# (Another separate figure)

# Plot Type
# 📌 Stem Plot
# Month-to-month sales changes for Product A

import matplotlib.pyplot as plt 
import numpy as np

#DATA
#Time Axis
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#Product Sales
product_A = [1200, 1500, 1700, 1600, 1800, 2000]

#FONTS
font1 = {"family": "verdana", "color" : "red", "size" : 20}
font2 = {"family": "serif", "color" : "green", "size" : 15}

plt.stem(months, product_A, linefmt = "b-.", markerfmt = "r", basefmt = "r")
plt.title("Discrete Analysis", fontdict = font1)
plt.xlabel("Months", fontdict = font2)
plt.ylabel("Product", fontdict = font2)
plt.show()
