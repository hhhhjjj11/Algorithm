# 정리
"""

"""
# 풀이
import sys
N  = int(input())

dp = [0]*(N+1) # dp[i] : 3*i까지의 
if N ==1:
    print(0)
    exit(0)
dp[2] = 3
if N == 2:
    print(3)
    exit(0)
dp[3] = 0
if N ==3:
    print(0)
    exit(0)
dp[4] = 11

if N>5:
    for i in range(5, N+1):
        if not i%2: 
            dp[i] = 2 + dp[i-2]*3 + dp[i-4]*2
            
            K = 3
            while True:
                if i-2*K <0:
                    break
                dp[i] += dp[i-2*K] * 2
                K += 1

print(dp[N])