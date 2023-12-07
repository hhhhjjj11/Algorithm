from random import randint
import random
# subprocess.call

# 예제 생성
def example():
    n, m = randint(1,3), randint(1,3)
    li = []
    for _ in range(n):
        temp = []
        for x in range(m):
            temp.append(randint(-100,100))
        li.append(temp)

    return n, m ,li

# 맞은 답
import sys
sys.setrecursionlimit(10**5)
from collections import deque

def right_sol(n, m, mat):

    # n, m = map(int, input().split())
    # mat = [list(map(int, input().split())) for _ in range(n)]

    dp = [[-1000000000] * m for _ in range(n)]
    left = [[-1000000000] * m for _ in range(n)]
    right= [[-1000000000] * m for _ in range(n)]


    #1 첫줄작업
    dp[0][0] = mat[0][0]
    c = 0
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + mat[0][j]
        c += 1

    for i in range(1, n):
        # 2 왼->오
        #2.1 left first

        left[i][0] = dp[i-1][0] + mat[i][0]
        for j in range(1, m):
            c += 1
            left[i][j] = max(dp[i-1][j]+mat[i][j], left[i][j-1]+mat[i][j])
        # 3 오 ->왼
        right[i][m-1] = dp[i-1][m-1] + mat[i][m-1]
        for j in range(m-2, -1, -1):
            right[i][j] = max(dp[i-1][j] + mat[i][j], right[i][j+1] + mat[i][j])
            c += 1
        #4 merge
        for j in range(m):
            dp[i][j] = max(right[i][j], left[i][j])
            c += 1
    # print(dp[n-1][m-1])
    return dp[n-1][m-1]
    

# 틀린 답
import sys

def wrong_sol(N, M, g):
    import sys
    sys.setrecursionlimit(int(1e6))
    # N, M = map(int,sys.stdin.readline().strip().split())
    # g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
    DP = [[[-int(1e9), -int(1e9), -int(1e9)] for _1 in range(M)] for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # DP[i][j] = i,j에서 N-1,M-1까지 가치최대

    # 왼, 오, 아래
    di = [0,0,1]
    dj = [-1,1,0]

    def DFS(i,j, dir): 
        # print(i,j,'/',dir)
        if i==N-1 and j==M-1:
            return g[N-1][M-1]
        
        if DP[i][j][dir] > -int(1e9):
            return DP[i][j][dir]

        MAX = -int(1e9)
        
        for k in range(3):
            i_next, j_next = i + di[k],j + dj[k]
            if 0<=i_next<N and 0<=j_next<M and not visited[i_next][j_next]:
                visited[i_next][j_next] = 1
                res = DFS(i_next,j_next,k)
                if MAX < res + g[i][j]:
                    MAX = res + g[i][j]
                visited[i_next][j_next] = 0
        # print(i,j,'/',dir,'종료')
        
        DP[i][j][dir] = MAX
        return MAX

    visited[0][0] =1
    DFS(0,0,1)
    DFS(0,0,2)
    # print(max(DP[0][0]))
    if N==1 and M==1 :
        return g[0][0]
    return max(DP[0][0])
# 반례 출력
def check():
    n, m, li = example()
    right = right_sol(n,m, li)
    wrong = wrong_sol(n,m, li)

    if right != wrong:
        print(n, m, li)

        print("맞은 답:", right)
        print("틀린 답:", wrong)
        return
    else:
        print(n, m,li)
        check()

check()