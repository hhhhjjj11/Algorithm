# 정리
"""
visited 랑 dp랑 따로 쓰니까 시간초과뜸;;

"""
# 풀이
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().strip().split())

g = [list(sys.stdin.readline().strip()) for _ in range(N)]

D = {'U':[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1]}

dp = [[-1]*M for _ in range(N)]

def EXIT(i,j):
    if dp[i][j] >0:
        # print(i,j,'에서 구해둔 값 있음')
        return dp[i][j]

    di, dj = D[g[i][j]]
    i_next, j_next = i + di , j + dj

    # 탈출가능
    if not (0<= i_next < N and 0<= j_next <M):
        dp[i][j] = 1
        return dp[i][j]
    
    if dp[i_next][j_next] == 0:
        dp[i][j] = False
        return dp[i][j]

    dp[i][j] = 0    
    dp[i][j] = EXIT(i_next,j_next)
    return dp[i][j]

cnt = 0

for i in range(N):
    for j in range(M):
        if dp[i][j] == -1:
            dp[i][j] = 0
            Bool = EXIT(i,j)
            if Bool:
                cnt += 1
        else:
            cnt += dp[i][j]
print(cnt)