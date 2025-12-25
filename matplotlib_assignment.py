# ==========================================
# MATPLOTLIB ASSIGNMENT
# Data Visualization using Python
# ==========================================

# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np


# --------------------------------------------------
# Question 1:
# Create a scatter plot using Matplotlib to visualize
# the relationship between two arrays x and y.
# --------------------------------------------------

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]

# Scatter plot shows relationship between x and y
plt.scatter(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot between X and Y")
plt.show()


# --------------------------------------------------
# Question 2:
# Generate a line plot to visualize the trend of
# values for the given data.
# --------------------------------------------------

# Line plot is used to show the trend of data
plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Plot Showing Trend")
plt.show()


# --------------------------------------------------
# Question 3:
# Display a bar chart to represent the frequency
# of each item in the given array categories.
# --------------------------------------------------

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]

# Bar chart compares values of different categories
plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart of Categories")
plt.show()


# --------------------------------------------------
# Question 4:
# Create a histogram to visualize the distribution
# of values in the array data.
# --------------------------------------------------

data = np.array([3, 7, 9, 15, 22, 29, 35])

# Histogram shows distribution of numerical data
plt.hist(data, bins=5)
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Histogram of Given Data")
plt.show()


# --------------------------------------------------
# Question 5:
# Show a pie chart to represent the percentage
# distribution of different sections.
# --------------------------------------------------

sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]

# Pie chart shows percentage distribution
plt.pie(sizes, labels=sections, autopct='%1.1f%%')
plt.title("Pie Chart Showing Percentage Distribution")
plt.show()
print("matplotib _assignmemt_completed")