import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q07():
    #print("q01")
    #Bar chart
    #Size 16.4 x 6.4 inches
    #File name (q01.png)
    #Instruction:
    #Define Total amount of transactions by transaction currency code
    path = 'C:\\computertooldata\\transactions.csv'
    df = pd.read_csv(path)
    #print(df.columns)
    df['transactionCurrencyCode'] = df['transactionCurrencyCode'].str.upper()
    df2 = df[df['shippingState'].notnull()]
    df3 = df2[df2['shippingCountry'].notnull()]

    #print(df3)
    df4 = df3.groupby('transactionCurrencyCode')['transactionAmountUSD'].sum().reset_index()
    df4['transactionAmountUSD'] = pd.to_numeric(df4['transactionAmountUSD'], errors='coerce')
    df4 = df4.sort_values('transactionAmountUSD', ascending= False)

    #print(df4)
    plt.figure(figsize=(16.4, 6.4))

    plt.xticks(rotation= 270, fontsize=10)
    plt.yticks(fontsize=10)

    fig, ax = plt.subplots()
    bar_container = ax.bar(df4['transactionCurrencyCode'], df4['transactionAmountUSD'])
    ax.set(ylabel='USD', xlabel='CurrencyCode', title='Total amount of transactions by transaction currency code',
           ylim=(0, 300000000))
    plt.xticks(rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    ax.bar_label(bar_container, fmt='{:,.0f}', fontsize=5, rotation=90)
    plt.show()

