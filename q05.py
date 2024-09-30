import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests
import yfinance as yf
def q05():
    #Line chart (plot) of “Adj Close” of stock in the given list
    #Size 10 x 7 inches
    #File name (plot05.png)
    #Instruction:
    #Stocks: Apple, Walmart, IBM, Micron Technology, Boeing, American Express
    #Plot the adj close price of stock since 1st Jan 2024
    tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

    # Fetch the data
    data = yf.download(tickers_list, '2024-1-1')['Adj Close']

    # Plot all the close prices
    ((data.pct_change() + 1).cumprod()).plot(figsize=(10, 7))
    plt.legend()
    plt.title("Close Value", fontsize=16)

    # Define the labels
    plt.ylabel('Cumulative Close Value', fontsize=14)
    plt.xlabel('Time', fontsize=14)

    # Plot the grid lines
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.show()

