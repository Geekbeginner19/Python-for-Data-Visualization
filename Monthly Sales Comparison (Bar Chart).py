# 📊 PROJECT 2 — Monthly Sales Comparison (Bar Chart)
# 🎯 Goal

# Practice:
# Bar charts
# Mean and standard deviation
# Comparing values across categories

# 🧠 Scenario
# You are reviewing monthly sales to understand:
# Best performing month
# Average sales
# Sales variability

import matplotlib.pyplot as plt
import statistics as stats 

#Dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1700, 1600, 1800, 2000]

font1 = {"family": "verdana", "color" : "red", "size" : 20}
font2 = {"family": "serif", "color" : "green", "size" : 15}

plt.title("Monthly Sales Comparison", fontdict=font1)
plt.xlabel("Months", fontdict=font2)
plt.ylabel("Sales", fontdict=font2)

mean = stats.mean(sales)
standardDev = stats.stdev(sales)

print(f"Mean of the Monthly Sales Comparison: {round(mean)}")
print(f"Standard Deviation of the Monthly Sales Comparison: {round(standardDev)}")

plt.bar(months, sales, color = "blue", alpha = 0.5, edgecolor = "black")
plt.axhline(mean, color = "g", linestyle = "dashed", label = "Mean")
plt.axhline(mean + standardDev, color = "b", linestyle = "dashed", label = "Standard Deviation before Mean")
plt.axhline(mean - standardDev, color = "b", linestyle = "dashed", label = "Standard Deviation after Mean")
plt.legend(title = "Mean & Standard Deviation")
plt.show()
