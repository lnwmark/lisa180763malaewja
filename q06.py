import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q06():
    #print("q01")
    #Output:
    #Pie chart
    #Default size
    #File name (pie06.png)
    #Instruction:
    #Define the pie chart of product categories.
    BASE_URL = 'https://fakestoreapi.in/'
    response = requests.get(BASE_URL + "api/products")
    data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])

    df3 = df2['category'].unique()
    num_product_category = df2['category'].value_counts().tolist()

    # plot
    x = [1, 2, 3, 4]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

    fig, ax = plt.subplots()
    ax.pie(num_product_category, labels=(df3), colors=(colors), radius=3, center=(4, 4),
           wedgeprops={"linewidth": 1, "edgecolor": "white"}, textprops={'fontsize': 15},
           autopct='%1.f%%')

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))


    plt.show()