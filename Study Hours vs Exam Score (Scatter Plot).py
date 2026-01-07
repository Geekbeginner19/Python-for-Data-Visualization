# 🔬 Scatter Project 1: Study Hours vs Exam Score
# 🎯 Goal
# Check correlation between study time and performance.

# 📁 Data Example
# 20 students
# Study Hours: [1, 2, 3, 4, 5, 6, ...]
# Exam Score: [45, 50, 55, 65, 70, 78, ...]

# 🔍 Insight
# Strength of correlation

import matplotlib.pyplot as plt
import numpy as np 

ExamScores = np.random.normal(45, 85, 100)
StudyHours = np.random.normal(5, 10, 100)
color = np.random.uniform(0, 1, 100) #Randomising colors 

font1 = {"family" : "serif", "color" : "blue", "size" : 20}
font2 = {"family" : "verdana", "color" : "green", "size" : 15}

#Adding Color Conditions
# colorCondition = ExamScores > 70
# colors = np.where(colorCondition, "blue", "red")

plt.scatter(ExamScores, StudyHours, c = color, cmap = "viridis") #adding cmaps 
plt.colorbar() #Adding a color bar
plt.xlabel("Exam Scores", fontdict = font2)
plt.ylabel("Study Hours", fontdict = font2)
plt.title("Study Hours vs Exam Score", fontdict = font1)
plt.show()

