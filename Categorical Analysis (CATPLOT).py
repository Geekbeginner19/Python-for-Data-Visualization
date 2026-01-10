# 🧩 PART 1 — Categorical Analysis (CATPLOT)
# 📊 Objective
# Understand how tipping differs across categories.

# 🔧 Task
# Create a categorical plot that shows:
# Average tip amount
# Grouped by day
# Split by sex
# Separate panels for Lunch vs Dinner

# 🔍 Plot Type

# catplot(kind="bar")
# 📌 Questions this plot should answer:
# Which day has the highest average tips?
# Do males or females tip more on average?
# Does tipping behavior differ between lunch and dinner?

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

time = ["lunch", "dinner"]
sns.catplot(data = tips, x = "day", y = "tip", hue = "sex", kind = "bar", col = "time")

plt.suptitle("Average Tip Amount by Day, Sex, and Time")
sns.set_theme(style="whitegrid")
plt.show()