# 정리
"""
DP의 인자: 현재노드와 남은 시간(소요시간)
DP[i][j] = i번 건물에서 D-j분이 남았을때 가능한 경로의 수
DFS(i, time)  = DP[i][j]
"""
# 풀이
import sys

D = int(input())
# 정보관 0
g = [[1,2],[0,2,3],[0,1,3,4],[1,2,4,5],[2,3,5,7],[3,4,6],[5,7],[4,6]]

def DFS(i,remaintime):
    if remaintime == D-1:   # 1분남음. 이제 반드시 돌아가야만함.
        if not 0 in g[i]:
            return 0
        else: # 0으로 돌아갈 수 있으면
            return 1

print(DFS(0,D))