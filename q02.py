import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
def q02():
    #print("q01")
    #Horizontal Bar chart
    #Size 6.4 x 50.4 inches
    #File name (mychart02.png)
    #Instruction:
    #Display VISA transaction amounts by shipping country
    #(Optional) Please do not forget to uppercase shipping country letters
    path = 'C:\\computertooldata\\transactions.csv'
    df = pd.read_csv(path)
    print(df.columns)
    df2 = df[df['shippingState'].notnull()]
    df3 = df2[df2['shippingCountry'].notnull()]
    df4 = df3[df3['cardType'].notnull()]
    df4['cardType'] = df4['cardType'].str.upper()
    df4['shippingCountry'] = df4['shippingCountry'].str.upper()
    df5 = df4.query("cardType in ('VISA')")
    df6 = df5.groupby('shippingCountry')['transactionAmountUSD'].sum().reset_index()
    df6['transactionAmountUSD'] = pd.to_numeric(df6['transactionAmountUSD'], errors='coerce')

    df6 = df6.sort_values('transactionAmountUSD', ascending=True)
    #print(df6)
    plt.figure(figsize=(6.4,50.4))
    #plt.barh(df6['shippingCountry'], df6['transactionAmountUSD'])
    fig, ax = plt.subplots()
    bar_container = ax.barh(df6['shippingCountry'], df6['transactionAmountUSD'])
    ax.set(ylabel='Country', xlabel='USD in hundred millions', title='VISA transaction amounts by shipping country', xlim=(0, 200000000))
    plt.yticks(fontsize=4)
    ax.bar_label(bar_container,fmt='{:,.0f}', fontsize=4)
    plt.show()

