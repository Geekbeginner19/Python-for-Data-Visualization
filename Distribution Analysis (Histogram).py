# 🟩 FIGURE 2 — DISTRIBUTION ANALYSIS
# You must create a new figure, not a subplot.

# Plot Type
# 📊 Histogram
# Combined sales of Product A and B
# Mean line included

import matplotlib.pyplot as plt 
import numpy as np

#DATA
#Product Sales
product_A = [1200, 1500, 1700, 1600, 1800, 2000]
product_B = [1000, 1100, 1300, 1400, 1500, 1700]

font1 = {"family": "verdana", "color" : "red", "size" : 20}
font2 = {"family": "serif", "color" : "green", "size" : 15}

#ONLY MEAN NEEDED
combProd = product_A + product_B #Combined Sales of Products, A and B
mean = np.mean(combProd)
# standardDev = np.std(combProd)

plt.hist(combProd, color = "green", label = "Combined Product Sales", alpha = 0.8, edgecolor = "black")
plt.axvline(mean, color = "k", linestyle = "dashed", label = "Mean Line")
# plt.axvline(mean + standardDev, color = "r", linestyle = "dashed", label = "std+")
# plt.axvline(mean - standardDev, color = "g", linestyle = "dashed", label = "std-")
plt.legend()
plt.title("Product Distribution Analysis", fontdict = font1)
plt.xlabel("Products Sales", fontdict = font2)
plt.ylabel("Count", fontdict = font2)
plt.show()

