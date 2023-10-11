# 정리
"""
올라갔다가 내려오니까...
"""
# 풀이
import sys

N = int(input())
li = list(map(int,input().split()))

dp = [[1,1] for _ in range(N)]          # 첫 항: 증가 상태 cnt / 2항 : 감소상태 cnt
dp[0][0]= 1
dp[0][1] = 1
for i in range(N):
    for j in range(i):
        if li[i] > li[j] and dp[i][0] < dp[j][0]+1:
            dp[i][0] = dp[j][0] + 1

        elif li[i] < li[j]:
            if dp[j][1] + 1 > dp[i][1]:
                dp[i][1] = dp[j][1] + 1
            if dp[j][0] + 1 > dp[i][1]:
                dp[i][1] = dp[j][0] + 1 
# print(dp)
res = 0
for i in range(N):
    for j in range(2):
        if dp[i][j] > res:
            res = dp[i][j]
print(res)
