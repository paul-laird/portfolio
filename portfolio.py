def getPrice(sym):
    results=requests.get('https://query1.finance.yahoo.com/v8/finance/chart/%s'%sym)
    return json.loads(results.content)['chart']['result'][0]['meta']['regularMarketPrice']

class Portfolio:
    def __init__(self):
        self.__balance={}
        
    def invest(self,sym,qty):
        if qty<0:
            raise ValueError()
        self.__balance[sym]=self.getBalance(sym)+qty
            
    def divest(self,sym,qty):
        if qty<0 or qty>self.__balance[sym]:
            raise ValueError()
        self.__balance[sym]=self.getBalance(sym)-qty
            
    def getBalance(self,sym):
        if sym not in self.__balance:
            return 0
        return self.__balance[sym]
    
    def value(self):
        total=0
        for k,v in self.__balance.items():
            total+=v*getPrice(k)
        return total
