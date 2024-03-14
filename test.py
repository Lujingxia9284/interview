n, v = map(int, input().split(' '))
value, weight = [], []

for i in range(n):
    a, b = map(int, input().split(' '))
    value.append(a)
    weight.append(b)

dp = [[0]*(v+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, v+1):
        if weight[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i-1]]+value[i-1])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])


dp = [0]* (v+1)
for i in range(1, v+1):
    dp[i]=0
    for j in range(n):
        if weight[j] <=i:
            dp[i] = max(dp[i], dp[i-weight[j]] + value[j])

res = dp[v] if dp[v]!=0 else 0

print(res)