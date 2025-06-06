coins=[500,100,200,5,2,1,50,10,5,20]
coins.sort(reverse=True)
amount=int(input("Enter the amount:"))
res=[]
for coin in coins:
    while(amount>0):
        res.append(coin)
        amount=amount-coin
    if amount==0:
        break
print(res)
