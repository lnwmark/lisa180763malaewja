import matplotlib.pyplot as plt
import pandas as pd


def q03():
    #print("q01")
    #Bar chart
    #Size 6.4 x 50.4 inches
    #File name (mychart03.png)
    #Instruction:
    #Add columns to CSV file.
    #Define total spending by card type (Field: cardType)
    #Add chart decorations
    path = 'C:\\computertooldata\\transactions.csv'
    df = pd.read_csv(path)
    df['cardType'] = df['cardType'].str.upper()
    df2 = df[df['shippingCountry'].notnull()]
    df3 = df2[df2['cardType'].notnull()]
    df4 = df3[df3['shippingState'].notnull()]
    df5 = df4.groupby('cardType')['transactionAmountUSD'].sum().reset_index()
    df5['transactionAmountUSD'] = pd.to_numeric(df5['transactionAmountUSD'], errors='coerce')
    df5 = df5.sort_values('transactionAmountUSD', ascending=False)
    #print(df4)
    plt.Figure(figsize=(6.4,50.4))
    bar_labels = ['yellow', 'blue', 'green', 'red', 'orange']
    bar_colors = ['yellow', 'blue', 'green', 'red', 'orange']
    fig, ax = plt.subplots()
    bar_container = ax.bar(df5['cardType'], df5['transactionAmountUSD'], label=bar_labels, color=bar_colors)
    ax.set(ylabel='USD (in million)', xlabel='Card Type', title='Transaction amount by Card Type', ylim=(0, 400000000))
    ax.bar_label(bar_container, fmt='{:,.0f}')

    plt.show()
