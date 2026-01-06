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

ExamScores = np.random.randint(45, 85, 10)
StudyHours = np.random.randint(5, 10, 10)

font1 = {"family" : "serif", "color" : "blue", "size" : 20}
font2 = {"family" : "verdana", "color" : "green", "size" : 15}

plt.scatter(StudyHours, ExamScores, color = "r")
plt.xlabel("StudyHours", fontdict = font2)
plt.ylabel("Exam Scores", fontdict = font2)
plt.title("Study Hours vs Exam Score", fontdict = font1)
plt.show()

