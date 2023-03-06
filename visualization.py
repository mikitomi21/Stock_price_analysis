from ecofunction import macd, ema, signal
from trader import Trader, Share

Kuba = Trader(1000)
Kuba.buy_share(100, 82.5)
Kuba.buy_share(150, 40)

print(Kuba.get_money_account())
share = Kuba.get_shares()

for i in share:
    print(i)
