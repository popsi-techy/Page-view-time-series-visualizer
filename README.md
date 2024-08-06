# Page View Time Series Visualizer
visualized time series data using a line chart, bar chart and box plots. Used Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations helped me understand the patterns in visits and identify yearly and monthly growth.

Used the data to complete the following tasks:

- Used Pandas to import the data from "fcc-forum-pageviews.csv". 
- Cleaned the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
- Created a line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png".
- Created a bar_plot function that draws a bar chart similar to "examples/Figure_2.png".
- Created a box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png".
