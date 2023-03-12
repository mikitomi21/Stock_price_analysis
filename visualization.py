import pandas as pd
from ecofunction import macd, ema, signal
from trader import Trader, Share
from chart import show_chart

START_MONEY_ACCOUNT = 1000
START_DAY = 100
END_DAY = 103


Player = Trader(START_MONEY_ACCOUNT)
intel_value = pd.read_csv("intc_us_d.csv").iloc[START_DAY:]
intel_value['Srednia'] = (intel_value['Otwarcie'] + intel_value['Zamkniecie'])/2


rating = []
rating.append([macd(intel_value.iloc[START_DAY:START_DAY-50:-1]), signal(intel_value.iloc[START_DAY:START_DAY-50:-1])])
money_after_sold = [START_MONEY_ACCOUNT]
day = 0

while True:
    #if (input("Click q to exit. Click enter to continue: ") == 'q'):
    #    break

    if (day+START_DAY == 980):
        break

    #Next day
    rating.append([macd(intel_value.iloc[day+START_DAY:day+START_DAY-50:-1]), signal(intel_value.iloc[day+START_DAY:day+START_DAY-50:-1])])
    day += 1

    #Buy
    if(rating[day-1][0] <= rating[day-1][1] and rating[day][0] > rating[day][1]):
        price = Player.get_money_account()*0.1 + 100
        rate = intel_value['Srednia'].iloc[day+START_DAY]
        Player.buy_share(price, rate)

        #print(f"Player buy shade for: {price} with rating: {rate}. Your money account is {Player.get_money_account()}")

    #Sell
    elif (rating[day-1][0] >= rating[day-1][1] and rating[day][0] < rating[day][1]):
        rate = intel_value['Srednia'].iloc[day+START_DAY]
        Player.sell_all_shares(rate)
        money_after_sold.append(Player.get_money_account())

        #print(f"Player sold all shares. Your money account is {Player.get_money_account()}")
    
    
    
Player.sell_all_shares(rate)
print(f"End of the visualization. Your money account is {Player.get_money_account()}")

show_chart(money_after_sold)

