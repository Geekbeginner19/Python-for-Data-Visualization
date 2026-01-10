# 🧩 PART 3 — Trend Analysis (LINEPLOT)
# 📉 Objective
# Analyze tipping trends over time-like categories.

# 🔧 Task
# Create a line plot showing:
# Average tip
# Across days of the week
# Separate lines for Lunch vs Dinner
# Use markers for clarity

# 🔍 Plot Type
# lineplot

# 📌 Questions this plot should answer:
# On which days do tips peak?
# Does dinner consistently produce higher tips than lunch?
# Are trends stable or fluctuating?

import matplotlib.pyplot as plt
import seaborn as sns 

tips = sns.load_dataset("tips")

sns.lineplot(data = tips, x = "day", y = "tip", estimator = "mean", markers = True, style = "time", hue = "time")

# Titles and labels
plt.title("Average Tip Trend Across Days (Lunch vs Dinner)")
plt.xlabel("Day of the Week")
plt.ylabel("Average Tip Amount")

plt.show()