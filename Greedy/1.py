coin = [500, 100, 50, 10]
N = int(input())
tot = 0
for charge in coin:
    tot += N//charge
    N %= charge
print(tot)
