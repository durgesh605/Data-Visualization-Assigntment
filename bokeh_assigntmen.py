# ==========================================
# BOKEH ASSIGNMENT
# (Use Bokeh for the visualization of the given questions)
# ==========================================

# Importing required libraries
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256


# --------------------------------------------------
# Question 1:
# Create a Bokeh plot displaying a sine wave.
# Set x-values from 0 to 10 and y-values as the sine of x.
# --------------------------------------------------

x = np.linspace(0, 10, 100)
y = np.sin(x)

p = figure(title="Sine Wave using Bokeh",
           x_axis_label="X values",
           y_axis_label="Sin(X)")

p.line(x, y, line_width=2)
show(p)


# --------------------------------------------------
# Question 2:
# Create a Bokeh scatter plot using randomly generated
# x and y values. Use different sizes and colors for
# the markers based on the 'sizes' and 'colors' columns.
# --------------------------------------------------

# Generating random data
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.randint(5, 20, 50)
colors = np.random.rand(50)

source_data = {
    'x': x,
    'y': y,
    'sizes': sizes,
    'colors': colors
}

p = figure(title="Bokeh Scatter Plot with Size and Color")

p.scatter(
    x='x',
    y='y',
    size='sizes',
    fill_color=linear_cmap('colors', Viridis256, 0, 1),
    source=source_data
)

show(p)


# --------------------------------------------------
# Question 3:
# Generate a Bokeh bar chart representing the counts
# of different fruits using the given dataset.
# --------------------------------------------------

fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

p = figure(x_range=fruits,
           title="Fruit Count Bar Chart",
           x_axis_label="Fruits",
           y_axis_label="Count")

p.vbar(x=fruits, top=counts, width=0.6)
show(p)


# --------------------------------------------------
# Question 4:
# Create a Bokeh histogram to visualize the distribution
# of the given data.
# --------------------------------------------------

data_hist = np.random.randn(1000)

# Calculating histogram
hist, edges = np.histogram(data_hist, bins=30)

p = figure(title="Histogram using Bokeh",
           x_axis_label="Values",
           y_axis_label="Frequency")

p.quad(top=hist,
       bottom=0,
       left=edges[:-1],
       right=edges[1:])

show(p)


# --------------------------------------------------
# Question 5:
# Create a Bokeh heatmap using the provided dataset.
# --------------------------------------------------

data_heatmap = np.random.rand(10, 10)

x = [str(i) for i in range(10)]
y = [str(i) for i in range(10)]

heatmap_data = {
    'x': np.repeat(x, 10),
    'y': np.tile(y, 10),
    'value': data_heatmap.flatten()
}

p = figure(title="Heatmap using Bokeh",
           x_range=x,
           y_range=y,
           tools="hover",
           tooltips=[("Value", "@value")])

p.rect(
    x='x',
    y='y',
    width=1,
    height=1,
    source=heatmap_data,
    fill_color=linear_cmap(
        'value',
        Viridis256,
        data_heatmap.min(),
        data_heatmap.max()
    ),
    line_color=None
)

show(p)
print("Bokeh_assigntment_completed")