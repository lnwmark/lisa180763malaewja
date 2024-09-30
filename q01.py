import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
def q01():
    #Define number of US transactions by states
    #Bar chart
    #Size 20.4 x 6.4 inches
    #File name (mychart01.png)

    path = 'C:\\computertooldata\\transactions.csv'
    df = pd.read_csv(path)
    #print(df.columns)
    df2 = df[df['shippingCountry'].notnull()]
    df2['shippingCountry'] = df2['shippingCountry'].str.upper()
    df3 = df2.query("shippingCountry in ('US')")
    df3['shippingState'] = df3['shippingState'].str.upper()
    df4 = df3.groupby('shippingState')['transactionID'].count().reset_index()
    df4['transactionID'] = pd.to_numeric(df4['transactionID'], errors='coerce')
    df4 = df4.sort_values('transactionID',ascending= True)
    #print(df4)

    plt.figure(figsize=(20.4, 6.4))
    plt.bar(df4['shippingState'], df4['transactionID'], color='red')
    plt.ylabel('The number of Transaction')
    plt.xlabel('State in US')
    plt.title('The number of US transactions by states')
    plt.xticks(rotation= 90)
    plt.show()
