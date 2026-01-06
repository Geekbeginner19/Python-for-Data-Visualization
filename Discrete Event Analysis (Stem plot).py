# Daily Temperature Deviations
# 🎯 Goal
# Show how daily temperature differs from the weekly average.

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
tempvalues = [-2, -1, 0, 1, 2, -3, 1, 0, 2, 3, -1, -2, 1, 0]

font1 = {"family" : "serif", "color" : "blue", "size" : 20}
font2 = {"family" : "verdana", "color" : "green", "size" : 15}

plt.stem(days, tempvalues, linefmt = "r:", markerfmt = "ro", basefmt = "b--")
plt.xlabel("Days", fontdict = font2)
plt.ylabel("Temperature Values", fontdict = font2)
plt.title("Daily Temperature Deviations", fontdict = font1)
plt.show()