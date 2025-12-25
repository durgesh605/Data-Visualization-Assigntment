# ==========================================
# SEABORN ASSIGNMENT
# (Use Seaborn for the visualization of the given questions)
# ==========================================

# Importing required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# --------------------------------------------------
# Question 1:
# Create a scatter plot to visualize the relationship
# between two variables, by generating a synthetic dataset.
# --------------------------------------------------

# Generating synthetic dataset
df = pd.DataFrame({
    'X': np.random.rand(50),
    'Y': np.random.rand(50)
})

# Scatter plot using Seaborn
sns.scatterplot(x='X', y='Y', data=df)
plt.title("Scatter Plot using Synthetic Dataset")
plt.show()


# --------------------------------------------------
# Question 2:
# Generate a dataset of random numbers.
# Visualize the distribution of a numerical variable.
# --------------------------------------------------

# Generating random dataset
data = np.random.normal(0, 1, 1000)

# Distribution plot
sns.histplot(data, kde=True)
plt.title("Distribution of Numerical Variable")
plt.show()


# --------------------------------------------------
# Question 3:
# Create a dataset representing categories and their
# corresponding values.
# Compare different categories based on numerical values.
# --------------------------------------------------

# Creating category dataset
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [25, 40, 30, 35, 20]
})

# Bar plot for category comparison
sns.barplot(x='Category', y='Value', data=df)
plt.title("Comparison of Categories based on Values")
plt.show()


# --------------------------------------------------
# Question 4:
# Generate a dataset with categories and numerical values.
# Visualize the distribution of a numerical variable
# across different categories.
# --------------------------------------------------

# Creating dataset
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], 100),
    'Value': np.random.randint(10, 100, 100)
})

# Box plot for distribution across categories
sns.boxplot(x='Category', y='Value', data=df)
plt.title("Distribution of Numerical Values across Categories")
plt.show()


# --------------------------------------------------
# Question 5:
# Generate a synthetic dataset with correlated features.
# Visualize the correlation matrix of a dataset
# using a heatmap.
# --------------------------------------------------

# Creating synthetic correlated dataset
data = pd.DataFrame(np.random.rand(10, 10))

# Heatmap for correlation matrix
sns.heatmap(data.corr(), annot=True)
plt.title("Correlation Matrix Heatmap")
plt.show()
print("seaborn_assignment_completed")
# Seaborn assignment completed
