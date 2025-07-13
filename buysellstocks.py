n=int(input())
stock=list(map(int,input().split()))
min_price=stock[0]
maxprofit=0

for i in stock:
    profit=i-min_price
    maxprofit=max(maxprofit,profit)
    min_price=min(min_price,i)
print(maxprofit)    
