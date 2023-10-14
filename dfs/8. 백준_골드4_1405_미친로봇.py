# 정리
"""
한방에 맞혀 보리기.
"""
# 풀이
import sys
n, E, W, S, N = map(int,sys.stdin.readline().strip().split())
P= [E/100, W/100, S/100, N/100]

visited=[[0]*30 for _ in range(30)]
visited[15][15] = 1

di = [0,0,1,-1]
dj = [1,-1,0,0]  # 동 서 남 북

p_total = 0
def dfs(i,j,cnt, p):
    
    global p_total

    if cnt == n:
   
        p_total += p
        return
    
    for k in range(4):
        i_next, j_next = i+di[k], j+dj[k]
        if not visited[i_next][j_next]:
            visited[i_next][j_next] = 1
            dfs(i_next,j_next,cnt+1, p*P[k])
            visited[i_next][j_next] = 0

dfs(15,15, 0, 1)
print(p_total)