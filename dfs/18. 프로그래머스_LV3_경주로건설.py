# 정리
"""
왜 bottom up으로 하면 안되는 거지? 
1. botom up 으로 풀면 -> dfs(i,j) = i,j에서 도착지점까지 최소 비용
+ dp에 값이 있으면 탐색하지 않고 그 값을 그냥 리턴함. (그렇지 않으면..? 그렇지않으면 ....음... )
다음 칸에서 계산한 값이 정답케이스의 일부가 된다.

2. 그런데 이거는 틀렸음 왜냐하면


bottom up 으로 풀었던 문제 경로의 갯수

bottom up 문제가 회전을 포함 못시키는것같은데 바텀업으로도 될것같은데??

"""
# 풀이
import sys
sys.setrecursionlimit(10**6)

di = [0,0,1,-1]
dj = [1,-1,0,0]

def solution(board):
    print('sdfsdfsdfsdf')
    N = len(board)
    dp = [[[9999999,-1]]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    print('sdfsdfsdfsdf')
    def dfs(i,j,d_now): # dfs(i,j) = i,j 부터 도착지점까지 걸리는 비용
        print(i,j)
        if i==N-1 and j==N-1:
            return 0
        
        if not (i==0 and j==0) and visited[i][j]:
            print('반환',)
            return dp[i][j][0]
        
        for d in range(4):
            i_next, j_next = i + di[d] , j + dj[d]
            # 가본적이 없는 곳이면
            if 0<=i_next<N and 0<=j_next<N and board[i_next][j_next] != 1 and not visited[i_next][j_next]:
                # 방향이 같은 경우랑 다른경우 분기
                visited[i_next][j_next] =1
                TEMP = dfs(i_next,j_next,d)
                visited[i_next][j_next] = 0
                if d_now == d and TEMP+100 :  # 방향이 같은경우
                    
                    print('i,j', i,j, '/', 'i_next, j_next', i_next, j_next)
                    dp[i][j] = [TEMP+100, d]
                elif d_now != d: # 방향을 꺾는경우  # 값이 같아도 탐색 해야함
                    print('i,j', i,j, '/', 'i_next, j_next', i_next, j_next)
                    dp[i][j] = [TEMP+600, d]
            elif 0<=i_next<N and 0<=j_next<N and board[i_next][j_next] != 1 and visited[i_next][j_next]: #가본적이 있는곳
                # 만약에 방향이 다르면 + 500을 더함. 그리고 그 값이 현재 dp 값 보다 작으면 갱신.
                if dp[i_next][j_next][1] != d_now:
                    if dp[i_next][j_next][0] + 600 < dp[i][j][0]:
                        print('i,j', i,j, '/', 'i_next, j_next', i_next, j_next)
                        dp[i][j] = [dp[i_next][j_next][0] + 600, d_now]
                # 만약에 방향이 같으면 100을 더해보고. 그리고 그 값이 현재 dp 값보다 작으면 갱신.
                else:
                    if dp[i_next][j_next][0] + 100 < dp[i][j][0]:
                        print('i,j', i,j, '/', 'i_next, j_next', i_next, j_next)
                        dp[i][j] = [dp[i_next][j_next][0] + 100, d_now]

        return dp[i][j][0]
    print('sdfsdfsdfsdf')
    dp[0][0][1] = 0
    dfs(0,0,0)
    dp[0][0][1] = 2
    dfs(0,0,2)
    print('sdfsdfsdfsdf')
    return dp[0][0][0]

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))

# # 풀이
# import sys
# sys.setrecursionlimit(10**6)

# di = [0,0,1,-1]
# dj = [1,-1,0,0]

# def solution(board):
#     N = len(board)
#     dp = [[9999999]*N for _ in range(N)]
    
#     def dfs(i,j,d_now,V): # dfs(i,j) = i,j 부터 도착지점까지 걸리는 비용
#         if dp[i][j] > V:
#             dp[i][j] = V

#         for d in range(4):
#             i_next, j_next = i + di[d] , j + dj[d]
#             if 0<=i_next<N and 0<=j_next<N and board[i_next][j_next] != 1:
#                 # 방향이 같은 경우랑 다른경우 분기
#                 if d_now == d and V+100 < dp[i_next][j_next]+600:  # 방향이 같은경우
#                     dfs(i_next,j_next,d, V+100)
#                 elif d_now != d and V+600 <= dp[i_next][j_next]: # 방향을 꺾는경우  # 값이 같아도 탐색 해야함
#                     dfs(i_next,j_next,d, V+600)

#     dfs(0,0,0,0)
#     dfs(0,0,2,0)

#     return dp[N-1][N-1]