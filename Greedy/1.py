n=int(input())
coin=[500,100,50,10]
tot=0
for change in coin:
    tot+=n//change
    n%=change
print(tot)