
# bottom up : 재귀함수의 리턴값 -> 현재칸에서 목표칸까지의 목표 값.
# 관계식A : 현재칸에서 목표칸 까지의 목표값 = '현재칸의 바로 다음 칸'에서 목표칸 까지의 목표값들을 모두 더한 값. 
# 이 문제의 경우 목표값이 바로 가능한 경로의 수 이므로 관계식 A를 그대로 적용 가능 한 것. 

import sys

M, N = map(int,sys.stdin.readline().strip().split())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j):

    # 탐색의 끝. 
    if i == M-1 and j == N-1:
        return 1
    
    # dp값이 -1 보다 크단 얘기는 앞서 실행된 재귀함수들에 의해 답이 구해졌음을 의미.
    # 즉, 다시말해 해당 지점으로부터 목표지점까지의 경로의 수가 이미 계산되었음을 의미.    
    if dp[i][j] > -1:
        return dp[i][j] # 따라서, 반복하여 재귀함수를 실행할 필요가 없음, 값을 그대로 반환.
    
    # [i,j]가 탐색해본적이 없는 칸이라면
    # 탐색(계산)을 이어나가야함.

    # 이때 dp[i][j] 가 -1로 되어있으니, 일단 0으로 바꿔주자.
    # dp[i][j]를 0이 아닌 -1로 둔 이유는 다음과 같다.
    #   - 어떤 지점에서 목표지점까지 가는 경로가 존재하지 않을 수 있다. 즉 탐색결과가 0인 경우임.
    #   - 그러므로 0을 미방문 표시로 처리하면 -> 이미 계산을 해서0이나온 것임에도 불구하고 계속 미방문으로 처리하게 되어 무한루프가 돌게 됨.
    dp[i][j] = 0

    for k in range(4):
        i_next, j_next = i + dx[k], j + dy[k]
        if 0<=i_next<M and 0<=j_next<N and graph[i][j] > graph[i_next][j_next]:
            # 이동가능 조건 적용
            
            # 현재지점에서 목표지점 까지 경로의 수는 그 다음칸들에서 이동한 값들을 모두 더한 값과 같음.
            dp[i][j] += dfs(i_next,j_next)
    
    # 하위 노드들에 대한 계산을 모두 끝마친 후임. 그러면 현재칸의 계산이 완료되어있으므로 이제 반환.
    return dp[i][j]

print(dfs(0,0))