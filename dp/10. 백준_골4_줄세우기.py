# 정리
"""
가장 적게 옮기는 방법 -> 가장 긴 증가하는 수열을 구하고 걔네빼고 나머지애들을 알맞게 옮겨주면 됨.
즉, 최소 이동횟수 = 수열 길이 - 가장 긴 증가하는 수열 길이
"""
# 풀이
import sys

N = int(input())

li = [int(input()) for _ in range(N)]
dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if li[j] < li[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

max = max(dp)
print(N-max)