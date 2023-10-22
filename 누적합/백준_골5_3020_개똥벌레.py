# 정리
"""

"""
# 풀이
import sys

N, H = map(int,sys.stdin.readline().strip().split())

dp = [0]*(H+1)
dp2 = [0]*(H+1)

for i in range(N):
    if i%2 == 0:
        # 석순
        h = int(input())
        dp[h] += 1
    else:
        # 종유석
        h = int(input())
        dp2[h] += 1

s = [0]*(H+1)
s[0] = 9999999
print('dp', dp)
print('dp2', dp2)

for i in range(1,H+1):
    if dp[i]:
        for x in range(dp[i]):
            for k in range(1, i+1):
                s[k] += 1
    if dp2[i]:
        for x in range(dp2[i]):
            for l in range(H, H-i,-1):
                s[l] += 1

print('s', s)

min = min(s)
cnt =0
for i in range(H+1):
    if min == s[i]:
        cnt += 1

print(min, cnt)