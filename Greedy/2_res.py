n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m % (k+1)

res = 0
res += (count)*first
res += (m-count)*second

print(res)
