import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q09():
    #print("q01")
    #Output:
    #Pie chart
    #Green color shade
    #File name (q03.png)
    #Instruction:
    #Define the pie chart of product brands.
    BASE_URL = 'https://fakestoreapi.in/'
    response = requests.get(BASE_URL + "api/products")
    data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])
    #print(df2[['id', 'title', 'category']])
    #print(df2.columns)
    # print(df2[['brand']])
    df2['brand'] = df2['brand'].str.upper()

    df3 = df2['brand'].unique()
    num_product_brand = df2['brand'].value_counts().tolist()

    # output
    # make data
    x = [1, 2, 3, 4]
    colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(x)))

    # plot
    fig, ax = plt.subplots()
    ax.pie(num_product_brand, labels=(df3), colors=colors, radius=3, center=(4, 4),
           wedgeprops={"linewidth": 1, "edgecolor": "black"}, textprops={'fontsize': 4},
           autopct='%1.f%%')

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()
    #path = 'C:\\A6511530\\' + 'q03.png'
    #plt.savefig(path)
