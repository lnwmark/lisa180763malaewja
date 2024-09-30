import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q08():
    #print("q01")
    #Output:
    #Horizontal Bar chart
    #File name (q02.png)
    #Instruction:
    #Display Mastercard transaction amounts by shipping state
    path = 'C:\\computertooldata\\transactions.csv'
    df = pd.read_csv(path)
    df['cardType'] = df['cardType'].str.upper()
    df2 = df[df['shippingState'].notnull()]
    df3 = df2[df2['shippingCountry'].notnull()]
    df3['shippingCountry'] = df3['shippingCountry'].str.upper()
    df3['shippingState'] = df3['shippingState'].str.upper()
    df4 = df3.query("shippingCountry in ('US')")
    df5 = df4.query("cardType in ('MC')")
    df5 = df4.groupby('shippingState')['transactionAmountUSD'].sum().reset_index()
    df5 = df5.sort_values('transactionAmountUSD', ascending= False)

    plt.figure(figsize=(6.4, 50.4))

    #plt.barh(df5['shippingState'],df5['transactionAmountUSD'])
    fig, ax = plt.subplots()
    bar_container = ax.barh(df5['shippingState'],df5['transactionAmountUSD'])
    ax.set(ylabel='State', xlabel='USD in ten millions', title='Mastercard transaction amounts by shipping state ',
           xlim=(0, 50000000))
    plt.yticks(fontsize=4.5)
    ax.bar_label(bar_container, fmt='{:,.0f}', fontsize=4.5)
    plt.show()
    plt.show()