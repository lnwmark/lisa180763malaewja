import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q10():
    #print("q01")
    #Histogram
    #10 bins
    #File name (q04.png)
    #Instruction:
    #Define histogram of transaction amount that have the transaction amount less than 1,000 USD
    path = 'C:\\computertooldata\\transactions.csv'
    df = pd.read_csv(path)
    df2 = df[df['shippingCountry'].notnull()]
    df3 = df2[df2['shippingState'].notnull()]
    df4 = df3.query("transactionAmountUSD < 1000")
    plt.figure(figsize=(10.4, 6.4))
    plt.hist(df4['transactionAmountUSD'], bins=10, edgecolor = 'black')
    plt.xlabel("The transaction amount")
    plt.ylabel("Frequency")
    plt.title("Histogram of transaction amount that have the transaction amount less than 1,000 USD")
    plt.show()
