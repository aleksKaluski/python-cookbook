"""
MATPLOTLIB — Data Visualization in Python
"""

# =====================================================================
# Importing matplotlib
# =====================================================================

import matplotlib.pyplot as plt
import numpy as np


# =====================================================================
# Basic plotting (line plot)
# =====================================================================

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()

# plot() draws a line graph by default


# =====================================================================
# Adding labels, title, legend
# =====================================================================

plt.plot(x, y, label="Data")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()


# =====================================================================
# Multiple lines on one plot
# =====================================================================

y2 = [5, 15, 20, 35]

plt.plot(x, y, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.show()


# =====================================================================
# Customizing plots
# =====================================================================

plt.plot(x, y, linestyle="--", marker="o")
plt.show()

# Common styles:
# linestyle: "-", "--", ":", "-."
# marker: "o", "s", "^", "x"


# =====================================================================
# Scatter plot
# =====================================================================

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()


# =====================================================================
# Bar chart
# =====================================================================

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

plt.bar(names, scores)
plt.title("Bar Chart")
plt.show()


# =====================================================================
# Histogram
# =====================================================================

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()

# Used to show distribution of data


# =====================================================================
# Subplots
# =====================================================================

plt.subplot(1, 2, 1)      # rows, columns, index
plt.plot(x, y)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.tight_layout()
plt.show()


# =====================================================================
# Figure and Axes (object-oriented approach)
# =====================================================================

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_title("OO Style Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.show()

# Preferred approach for complex plots


# =====================================================================
# Grid and limits
# =====================================================================

plt.plot(x, y)
plt.grid(True)
plt.xlim(0, 5)
plt.ylim(0, 40)
plt.show()


# =====================================================================
# Saving figures
# =====================================================================

plt.plot(x, y)
plt.savefig("plot.png")
plt.show()

# Save before show() for safety


# =====================================================================
# Common plot types (exam checklist)
# =====================================================================

plt.plot()        # line plot
plt.scatter()     # scatter plot
plt.bar()         # bar chart
plt.hist()        # histogram
plt.pie()         # pie chart


# =====================================================================
# Using NumPy with matplotlib
# =====================================================================

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.show()


# =====================================================================
# Typical exam mistakes to avoid
# =====================================================================

# - Forgetting plt.show()
# - Mixing OO and pyplot styles incorrectly
# - Wrong subplot indexing
# - Saving figure AFTER show()
