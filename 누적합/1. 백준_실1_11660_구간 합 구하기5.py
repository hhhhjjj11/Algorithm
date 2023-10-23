# 정리
"""
M=1 이면 반복문 돌리면 그만이겟지만
M이 존나 많으면 같은 계산을 존나 돌리는게 시간초과 유발요소임.
따라서 dp테이블 만들어서 계산 했던거 또 안하게 활용
"""
# 풀이
import sys
N, M = map(int ,sys.stdin.readline().strip().split())

g =[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = g[1][1]

for i in range(1, N+1):
    for j in range(1,N+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + g[i-1][j-1]


for _ in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().strip().split()))

    result  = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1] 
    print(result)
    
