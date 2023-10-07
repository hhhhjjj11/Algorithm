# 정리
"""

"""

# 풀이
import sys

N = int(input())

dp = [[0]*(N+1) for i in range(10)] 
for i in range(1,10):
    dp[i][1] = 1

for j in range(2,N+1):
    for i in range(10):
        if i == 0:
            dp[i][j] = dp[1][j-1]
        elif i == 9:
            dp[i][j] = dp[8][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]

res = 0
for i in range(10):
    res += dp[i][N]
print(res%1000000000)