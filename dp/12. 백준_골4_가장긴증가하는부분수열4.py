# 정리

# 풀이
import sys

N = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))
dp = [1]*N
temp = [[li[i]]for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if li[i] > li[j] and dp[j] + 1 > dp[i]:
            temp[i] = temp[j][:]
            temp[i].append(li[i])
            dp[i] = dp[j] + 1

max= max(dp)
I = dp.index(max)

print(max)
for i in temp[I]:
    print(i, end=" ")