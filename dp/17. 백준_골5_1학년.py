# 정리
"""
2차원 dp 테이블 만들어서
각 i에서 나올 수 있는값 전부 체크. 
dp[i][K] = i번째까지 계산해서 K가나오는 경우의 수


더하고 빼는거 경우의수 + 범위제한 -> 2차원 dp 테이블
범위제한 없으면 -> dictionary쓰면될듯??
"""

# 풀이
import sys

N = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))

dp = [[0]*21 for _ in range(N)]
dp[1][li[0]] = 1 

for i in range(2,N):
    # i=2이면
    for k in range(21):
        if dp[i-1][k]:   # 이전 까지 계산해서 k가 나오는 경우가 있으면
            if 0<= k + li[i-1] <=20:
                dp[i][k+li[i-1]] += dp[i-1][k]
            if 0<= k - li[i-1] <=20:
                dp[i][k-li[i-1]] += dp[i-1][k]

print(dp[N-1][li[-1]])