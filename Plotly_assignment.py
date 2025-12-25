# ==========================================
# PLOTLY ASSIGNMENT
# (Use Plotly for the visualization of the given questions)
# ==========================================

# Importing required libraries
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# --------------------------------------------------
# Question 4:
# Using the given x and y data, generate a 3D surface
# plot to visualize the function.
# --------------------------------------------------

# Generating x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Creating meshgrid
x, y = np.meshgrid(x, y)

# Calculating z values using the given function
z = np.sin(np.sqrt(x**2 + y**2))

# Creating 3D surface plot
fig = go.Figure(data=[go.Surface(z=z)])

fig.update_layout(
    title="3D Surface Plot using Plotly",
    scene=dict(
        xaxis_title="X values",
        yaxis_title="Y values",
        zaxis_title="Z values"
    )
)

fig.show()


# --------------------------------------------------
# Question 5:
# Using the given dataset, create a bubble chart to
# represent each country's population (y-axis),
# GDP (x-axis), and bubble size proportional
# to the population.
# --------------------------------------------------

# Creating dataset
df = pd.DataFrame({
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000, 5)
})

# Creating bubble chart
fig = px.scatter(
    df,
    x='GDP',
    y='Population',
    size='Population',
    color='Country',
    title="Bubble Chart: GDP vs Population"
)

fig.show()
print("Plotly_Assigntment_completed")