import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data from the CSV file
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data (if needed)
df = none;

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x=df.index, y='value', ax=ax)
    ax.set_title('Daily Value Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_bar, x='month', y='value', ci=None)
    ax.set_title('Monthly Bar Plot')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Value')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Value')

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig

# Test the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
