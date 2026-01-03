# 📊 PROJECT 1 — Student Score Distribution (Histogram)
# 🎯 Goal

# Practice:
# Creating histograms
# Choosing bin sizes
# Adding mean and standard deviation lines
# Labeling and styling for clarity

# 🧠 Scenario
# You are analyzing exam scores of students in a class to understand:
# Score distribution
# Average performance
# How spread out the scores are

import matplotlib.pyplot as plt
import statistics as stats 
import numpy as np

#dataset
scores = [
    45, 50, 52, 55, 58, 60, 62, 65, 68, 70,
    72, 75, 78, 80, 82, 85, 88, 90, 92, 95
]

font1 = {"family": "verdana", "color" : "red", "size" : 20}
font2 = {"family": "serif", "color" : "green", "size" : 15}

plt.title("Student Score Distribution", fontdict = font1)
plt.xlabel("Scores", fontdict = font2)
plt.xticks(np.arange(45, 100, 10))
plt.ylabel("Number of Students", fontdict = font2)
#plt.hist(scores, bins = 10, edgecolor = "black", color = "lightred")

mean = stats.mean(scores)
standardDev = stats.stdev(scores)

print(f"Mean of the Student scores is {mean}")

plt.hist(scores, bins = 10, edgecolor = "black", color = "green", alpha = 0.7)
plt.axvline(mean, color = "red", linestyle = "dashed", label = "Mean")
plt.axvline(mean + standardDev, color = "blue", linestyle = "dashed", label = "Standard Deviation before Mean")
plt.axvline(mean - standardDev, color = "blue", linestyle = "dashed", label = "Standard Deviation after Mean")
plt.legend(title = "Mean & Standard Deviation")
plt.show()