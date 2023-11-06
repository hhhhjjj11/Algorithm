# 정리
"""

"""
# 풀이
import sys

N = int(input())

li = list(map(int,sys.stdin.readline().strip().split()))

dp = [1]*N  # dp[i] : i번째항까지 증가하는 부분수열의 가장 긴 길이
 
for i in range(N):
    for j in range(i):
        if li[i] > li[j] and dp[j]+1>dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))