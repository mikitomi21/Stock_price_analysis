class Share():
    def __init__(self, price, rate):
        self.price = price
        self.rate = rate
    
    def __str__(self) -> str:
        
        return "Price: " + str(self.price) + " Rate: " + str(self.rate)
    

class Trader():
    def __init__(self,money_account):
        self.money_account = money_account
        self.shares = []
    
    def get_money_account(self):
        return self.money_account
    
    def get_shares(self):
        return self.shares
    
    def buy_share(self, price, rate):
        if (price > self.money_account):
            return
        self.money_account -= price
        share = Share(price, rate)
        self.shares.append(share)
