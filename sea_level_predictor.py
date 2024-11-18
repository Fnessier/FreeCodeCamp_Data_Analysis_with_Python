import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,10 ))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label= "original data")

    # Create first line of best fit
    y1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(df['Year'].min(),2051))
    plt.plot(years, y1.intercept + y1.slope*years, 'r', label='first line of best fit')

    # Create second line of best fit
    df2 = df.loc[df['Year']>=2000]
    y2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000,2051))
    plt.plot(years2, y2.intercept + y2.slope*years2, 'g', label='first line of best fit')

    # Add labels and title
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
