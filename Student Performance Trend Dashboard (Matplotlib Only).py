# 🎯 PROJECT: Student Performance Trend Dashboard (Matplotlib Only)

# 🧠 What You’re Building

# A multi-line performance visualization that shows how different students (or subjects)
# perform over time, with clean styling, labels, legends, and markers — like something you’d actually present.

# 📊 Project Scenario
# You are given test scores of 3 students across 6 tests in a semester.

# You must visualize:
# Each student’s performance trend
# Make the chart readable, professional, and informative

import matplotlib.pyplot as plt 

#Data
tests = [1, 2, 3, 4, 5, 6]

student_A = [65, 70, 72, 78, 85, 90]
student_B = [60, 62, 68, 75, 80, 82]
student_C = [55, 60, 63, 67, 72, 78]

#fonts for the graph titles, xlabels and ylabels
font1 = {"family" : "serif", "color" : "blue", "size" : 20}
font2 = {"family" : "verdana", "color" : "darkred", "size" : 15}

#Plot Styles (Inbuilt)
plt.style.use("seaborn-v0_8-paper")

plt.title("Student Performance Over Time", fontdict = font1)
plt.xlabel("Test Number", fontdict = font2)
plt.ylabel("Score (%)", fontdict = font2)

plt.plot(tests, student_A, color = "r", linestyle = "-", linewidth = 2, marker = "o", label = "StuA")
plt.plot(tests, student_B, color = "y", linestyle = "--", linewidth = 2, marker = "s", label = "StuB")
plt.plot(tests, student_C, color = "b", linestyle = ":", linewidth = 2, marker = ">", label = "StuC")

plt.legend()#Adding legends for more readability
plt.grid() #Adding a grid
plt.show()

#print(plt.style.available)