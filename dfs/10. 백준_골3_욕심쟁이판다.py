# 정리
"""
bottom up 으로
완탐돌리면 당연 시간초과

정리할게 존나 많은데
우선 
1. dp[i][j] = i,j에서 가장 많이 움직일 수 있는 칸의 갯수
2. 이미 탐색한 적이 있다면 -> 이미 거기서 해볼 수 있는건 다 해본 것 이기 때문에 
 그 값이 거기서 움직일 수 있는 최대임. 따라서 거기를 찍고 다시 계산할 필요X , 그냥 리턴.
더 계산 할 필요가 없다..
 
뭔가 잘 안와닿아. 왠지 그렇게 하면 안될것같아. 뭐 그런 생각이 든다.
왜 그렇게 하면 안될것 같냐면 -> 다음 칸의 기록을 그대로 갖다 써도 되는거 맞아? 그러면 안될 것같음

근데 맞음! 이유:  [ 이전 칸들 > 현재칸 > 다음칸 > 다음칸 기록에 반영된 그 다음 모든 칸들 ] 이므로 
이전 칸들이 다음칸의 기록에 영향을 미치지 않음. 따라서 그대로 갖다 써도 됨 



3. dp[i][j] 는 다음 칸의 dp + 1 과 기존의 dp값을 비교하여 더 큰 값으로 교체. 그렇게 최대값을 계속 갱신

"""

# 풀이
import sys

n = int(input())

g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

dp = [[0]*n for _ in range(n)] # dp[i][j] = i,j에서 최대이동 가능 칸 수

def dfs (i,j):

    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = 1

    for k in range(4):
        i_next, j_next = i + di[k], j + dj[k]

        if 0<=i_next<n and 0<=j_next< n and  g[i_next][j_next] > g[i][j]:
            dp[i][j] = max(dp[i][j], dfs(i_next,j_next)+1)  
    
    return dp[i][j]

answer = 0

for p in range(n):
    for q in range(n):
        answer = max(answer, dfs(p,q))

print(answer)