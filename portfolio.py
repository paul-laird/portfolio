prices={'MSFT':160,'AMZN':200}

class Portfolio:
    def __init__(self):
        self.__balance={}
        
    def invest(self,sym,qty):
        self.__balance[sym]=self.getBalance(sym)+qty
            
    def divest(self,sym,qty):
        self.__balance[sym]=self.getBalance(sym)-qty
            
    def getBalance(self,sym):
        if sym not in self.__balance:
            return 0
        return self.__balance[sym]
    
    def value(self):
        total=0
        for k,v in self.__balance.items():
            total+=v*prices[k]
        return total
