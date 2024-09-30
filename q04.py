import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests

def q04():
    #Histogram
    #Size 6=10.4 x 6.4 inches
    #File name (hit04.png)
    #Instruction:
    #Define histogram of price of the product that have the price less than 4,000


    BASE_URL = 'https://fakestoreapi.in/'
    response = requests.get(BASE_URL + "api/products")
    data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])
    df3 = df2.query("price < 4000")
    plt.figure(figsize=(10.4, 6.4))
    plt.hist(df3[['price']], edgecolor='white', linewidth=1.5)
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Histogram of price of the product that have the price less than 4,000')
    plt.show()
