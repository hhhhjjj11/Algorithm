# 정리
"""
1. dp에 무엇을 표시할 것인가 : [해당 인덱스 무게까지 채우는데 필요한 동전 갯수] 의 최소.
2. 어떤 경우에 갱신할 것인가 : 갯수가 더 적은 경우 갱신.

아 존나 헷갈리네 ssi bar~
"""
# 풀이
import sys

n, k = map(int, sys.stdin.readline().strip().split())

dp = [k+1]*(k+1)
dp[0] = 0
for _ in range(n):
    v = int(sys.stdin.readline().strip())
    if v <= k:
        for i in range(v, k+1):
            if dp[i-v] + 1 < dp[i]:
                dp[i] = dp[i-v] + 1

# print(dp)
if dp[k] == k+1:
    print(-1)
else:
    print(dp[k])