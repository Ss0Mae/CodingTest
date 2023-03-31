N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[N-1]
second = data[N-2]
res = 0
count = 0
tmp = first
for i in range(M):
    if (count == K):
        res += second
        count = 0
    else:
        res += first
        count += 1
print(res)
