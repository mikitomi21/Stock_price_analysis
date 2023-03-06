import pandas as pd
from ecofunction import macd, ema, signal
from trader import Trader, Share

START_MONEY_ACCOUNT = 1000

Player = Trader(START_MONEY_ACCOUNT)
intel_value = pd.read_csv("intc_us_d.csv").iloc[30:]

while True:
    if (input("Click q to exit. Click enter to continue: ") == 'q'):
        break
    #TODO 

print("End of the visualization. Your money account is ", Player.get_money_account())

