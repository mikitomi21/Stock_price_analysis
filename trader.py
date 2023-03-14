class Tax:
    NO = 1
    YES = 0.95


class Share:
    def __init__(self, price, rate):
        self.price = price
        self.rate = rate
    
    def __str__(self) -> str:
        
        return "Price: " + str(self.price) + " Rate: " + str(self.rate)
    

class Trader:
    def __init__(self,money_account, tax=Tax.YES):
        self.money_account = money_account
        self.tax = tax
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
    
    def sell_all_shares(self, current_rate):
        for share in self.shares:
            self.money_account += share.price * self.tax * current_rate / share.rate
        self.shares = []

