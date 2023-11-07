
N = int(input())

li = [0]*501
dp = [0]*501
for _ in range(N):
    i, v = map(int,input().split())
    li[i-1] = v
    dp[i-1] = 1



for i in range(1,501):
    for j in range(i):
        if li[i] > li[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1


print(N-max(dp))