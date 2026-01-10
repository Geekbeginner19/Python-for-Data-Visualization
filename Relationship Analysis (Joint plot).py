# 🧩 PART 2 — Relationship Analysis (JOINTPLOT)
# 📈 Objective

# Explore the relationship between total bill and tip.

# 🔧 Task
# Create a joint plot showing:
# total_bill vs tip
# Colored by smoker status
# Include a regression or KDE component

# 🔍 Plot Type
# jointplot(kind="scatter") or kind="reg"

# 📌 Questions this plot should answer:
# Do larger bills lead to higher tips?
# Is the relationship stronger for smokers or non-smokers?
# Are there visible clusters or outliers?

import matplotlib.pyplot as plt 
import seaborn as sns 

tips = sns.load_dataset("tips")
sns.jointplot(data = tips, x = "total_bill", y = "tip", kind = "scatter", hue = "smoker")#Hue Gives the Colors anad also acts as the legend

plt.show()