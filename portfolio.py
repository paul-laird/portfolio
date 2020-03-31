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

def popHighest(plist):    
    pvalues=[]
    index=0
    maxi=0
    maxindex=-1
    for item in plist:
        currentvalue=item.value()
        pvalues.append(currentvalue)
        if currentvalue>maxi:
            maxi=currentvalue
            maxindex=index
        index+=1
    return plist.pop(maxindex)


def sort(vlist):
    length=len(vlist)
    if length<2:
        return vlist
    half=length//2
    half2=length-half
    left=sort(vlist[0:half])
    right=sort(vlist[half:length])
    counter1=0
    counter2=0
    output=[]
    while counter1+counter2<length:
        if counter1<half and (counter2 == half2 or left[counter1][0]<right[counter2][0]):
            output.append(left[counter1])
            counter1+=1
        else:
            output.append(right[counter2])
            counter2+=1
    return output


def sort1(plist):
    valuedlist=[]
    for item in plist:
        valuedlist.append((item.value(),item))
    list2=sort(valuedlist)
    output=[]
    for t in list2:
        output.append(t[1])
    return output
