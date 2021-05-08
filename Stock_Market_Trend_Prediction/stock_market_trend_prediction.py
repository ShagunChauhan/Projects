# -*- coding: utf-8 -*-

"""
Python 3
@authors: Shagun Chauhan
Project: Stock Market Trend Prediction
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#load the data
apple = pd.read_csv('apple.csv')

#create the simple moving average with a 30 days window
SMA30 = pd.DataFrame()
SMA30['Close'] = apple['Close'].rolling(window=30).mean()
SMA100 = pd.DataFrame()
SMA100['Close'] = apple['Close'].rolling(window=100).mean()

#create a new data frame to store all the Data
data = pd.DataFrame()
data['APPLE'] = apple['Close']
data['SMA30'] = SMA30['Close']
data['SMA100'] = SMA100['Close']

#create a func to signal when to buy and sell the stock
def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['APPLE'][i])
                sigPriceSell.append(np.nan)
                flag=1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['APPLE'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return  (sigPriceBuy, sigPriceSell)


#store the buy and sell data into a variable
buy_sell_data = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell_data[0]
data['Sell_Signal_Price'] = buy_sell_data[1]

#visualize the data and market trend of buy and sell
plt.figure(figsize=(12.5,5.5))
plt.plot(data['APPLE'], label='APPLE Close Price', color='grey')
plt.plot(data['SMA30'], label ='SMA30', color='yellow')
plt.plot(data['SMA100'], label ='SMA100', color='purple')
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color='green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color='red')
plt.title('APPLE Close price history of buy and sell')
plt.xlabel('12 Aug, 2002 - 7 May, 2021')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
