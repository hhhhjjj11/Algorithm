# 정리
"""

"""

# 풀이
import sys
sys.setrecursionlimit(10**6)

di = [0,0,1,-1]
dj = [1,-1,0,0]

def solution(board):
    N = len(board)
    dp = [[9999999]*N for _ in range(N)]
    
    def dfs(i,j,d_now,V): # dfs(i,j) = i,j 부터 도착지점까지 걸리는 비용
        # print('i,j',i,j, '/', V)
        if dp[i][j] > V:
            dp[i][j] = V

        for d in range(4):
            i_next, j_next = i + di[d] , j + dj[d]
            if 0<=i_next<N and 0<=j_next<N and board[i_next][j_next] != 1:
                # 방향이 같은 경우랑 다른경우 분기
                if d_now == d and V+100 < dp[i_next][j_next]+600:  # 방향이 같은경우
                    dfs(i_next,j_next,d, V+100)
                    if i==1 and j==1 :
                        print('1', d_now, d, V, V+100)
                elif d_now != d and V+600 <= dp[i_next][j_next]: # 방향을 꺾는경우  # 값이 같아도 탐색 해야함
                    dfs(i_next,j_next,d, V+600)
                    if i==1 and j==1 :
                        print('2', d_now, d, V, V+600)

    dfs(0,0,0,0)
    dfs(0,0,2,0)
    # for row in dp:
    #     print(row)
    return dp[N-1][N-1]