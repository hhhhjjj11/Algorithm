# 정리
"""
명제이용 : 1~a 까지 합을 X로 나눈 나머지 = 1~b 까지 합을 X로 나눈 나머지  => a+1 ~ b 까지 합은 X로 나누어 떨어진다.

iteertools 이용하는 것보다 간단히 만든 식 쓰는게 빠르다. 툴 쓰면 시간초과난다... 아마 r=2여서 그런 것 같다.
"""

# 풀이
import sys
# from itertools import combinations

N, M = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))

dp = [0]*N
dp[0] = li[0] % M

count  = [0]*M
count[dp[0]%M] += 1
for i in range(1, N):
    dp[i] = (dp[i-1] + li[i]) % M
    count[dp[i]%M] += 1

result = count[0]

for i in range(M):
    if count[i] >= 2:
        result += (count[i] * (count[i]-1)) //2

print(result)