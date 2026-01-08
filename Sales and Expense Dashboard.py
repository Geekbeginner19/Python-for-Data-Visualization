#🟦 FIGURE 1 — SALES & EXPENSE DASHBOARD
# Subplot 1 (Top-Left)
# 📉 Line Plot
# Product A sales
# Product B sales
# Same axes
# Legend required

# Subplot 2 (Top-Right)
# 📊 Bar Chart
# Monthly revenue (Product A + B)

# Subplot 3 (Bottom-Left)
# 📊 Stackplot
# Rent
# Food
# Transport
# Entertainment

# Subplot 4 (Bottom-Right)
# 📈 Scatter Plot
# Ad spend vs Revenue

import matplotlib.pyplot as plt 

#DATA
#Time Axis
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#Product Sales
product_A = [1200, 1500, 1700, 1600, 1800, 2000]
product_B = [1000, 1100, 1300, 1400, 1500, 1700]
#Expense Breakdown
rent = [500, 550, 600, 650, 700, 750]
food = [200, 220, 210, 230, 250, 270]
transport = [80, 90, 85, 95, 100, 110]
entertainment = [60, 70, 65, 75, 80, 90]
#Marketing and Performance Data
ad_spend = [200, 250, 300, 350, 400, 450]
revenue = [2200, 2600, 3000, 3200, 3500, 3900]

#Initializing figures and axis with number of roles and columns and the figure number
fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize = (10, 6))
plt.subplots_adjust(hspace = 0.5, wspace = 0.5) #Adjusting the Height Space and Width Space between graphs
fig.suptitle("Business Performance Dashboard") #Title of the Dashboard

#Font styles for Title of Subplots
fontstyle = "italic"

#Line Graph (Top Left)
axs[0,0].plot(months, product_A, color = "r", linestyle = "-", marker = "o", label = "Product A")
axs[0,0].plot(months, product_B, color = "b", linestyle = ":", marker = "s", label = "Product B")
axs[0,0].set_xlabel("MONTHS", color = "g")
axs[0,0].set_ylabel("PRODUCT SALES", color = "g")
axs[0,0].legend()
axs[0,0].grid()
axs[0,0].set_title("Sales", fontstyle = fontstyle)


#Bar Graph (Top Right)
axs[0,1].bar(months, revenue, color = "g", alpha = 0.5)
axs[0,1].set_title("Monthly Revenue", fontstyle = fontstyle)
axs[0,1].set_xlabel("MONTHS", color = "g")
axs[0,1].set_ylabel("REVENUE", color = "g")


#Stackplot (Bottom Left)
axs[1,0].stackplot(months, rent, food, transport, entertainment, alpha = 0.8, labels = ["rent", "food", "transport", "entertainment"])
axs[1,0].set_title("Expense Breakdown", fontstyle = fontstyle)
axs[1,0].set_xlabel("MONTHS", color = "g")
axs[1,0].set_ylabel("EXPENSES", color = "g")
axs[1,0].legend(loc = "lower right", title = "Expense Breakdown")


#Scatter (Bottom Right)
axs[1,1].scatter(ad_spend, revenue, color = 'r')
axs[1,1].set_title("Ad Spent vs. Revenue", fontstyle = fontstyle)
axs[1,1].set_xlabel("AD SPENT", color = "g")
# axs[1,1].set_yticks([2200, 2600, 3000, 3200, 3500, 3900]) #yticks can be set too for better readability
axs[1,1].set_ylabel("REVENUE", color = "g")

plt.show()
