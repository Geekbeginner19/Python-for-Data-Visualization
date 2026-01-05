# Advanced Histogram Analysis
# (Advanced Histograms)
# 🎯 Goal

# Practice:
# Custom bin sizing
# Transparency (alpha)
# Multiple statistical markers
# Professional labeling
# Distribution comparison mindset

# 🧠 Scenario
# You are analyzing exam score distributions from two different classes to determine:
# Which class performed better overall
# Which class had more consistent performance
# How the distributions differ

import matplotlib.pyplot as plt
import numpy as np
import statistics as stats 

ClassAScores = np.arange(10, 310, 10)
ClassBScores = np.arange(10, 210, 10)

scores = ClassAScores + ClassBScores

font1 = {"family": "verdana", "color" : "red", "size" : 20}
font2 = {"family": "serif", "color" : "green", "size" : 15}

plt.xlabel("Score", fontdict = font2)
plt.ylabel("Frequency", fontdict = font2)
plt.hist([ClassAScores, ClassBScores], bins = 5, color = ["green", "orange"], label = ["Class A", "Class B"], alpha = 0.7)
plt.legend()
plt.title("Class Scores", fontdict = font1)
plt.show()


