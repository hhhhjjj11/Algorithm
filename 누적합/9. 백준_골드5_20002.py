# 정리
"""
        for k in range(1, min(i,j)+1):  이 부분 유의.
"""
# 풀이
import sys

N = int(input())

g =[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

sum = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum[i][j] = g[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

M = -99999999999
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, min(i,j)+1):  
            V = sum[i][j] - sum[i-k][j] - sum[i][j-k] + sum[i-k][j-k]
            if V > M:
                M = V

print(M)