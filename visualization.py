from ecofunction import macd, ema, signal
from trader import Trader, Share

Player = Trader(1000)

while True:
    if (input("Click q to exit. Click enter to continue: ") == 'q'):
        break

print("End of the visualization. Your money account is ", Player.get_money_account())

