# 정리
"""
1. 아이디어 위로올라가는 방향으로만 탐색 / 아래로올라가는 방향으로만 탐색
2. 아래 / 위로 탐색 마쳤을때 방문하지 않은 노드가남아있다면 해당 노드와는 대소 비교 불가능. 따라서 몇번째인지 알 수 없음.

오케이. 전략은 잘 잡았음. 굿.
그런데 이거를 내가 한것처럼 각각의 노드에 대해서 모두 dfs돌리면 시간초과뜸;;
한번에 각 노드에서 각 노드까지의 최단거리 를 구할 수 있는 알고리즘인 플로이드-와샬 이용해서 해결한다..

플로이드 와샬 직관적으로 이해가 안됨. 좀 많이 곱씹어 봐야할듯..
"""
# 풀이
import sys
sys.setrecursionlimit(10**5)
N,M = map(int, sys.stdin.readline().strip().split())

FW = [[0]*(N) for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    FW[a-1][b-1] = 1
    


# 간선의 가중치는 답을 구하는데 지장이 없으므로, 임의로 1로 두자.

for k in range(N):
    for i in range(N):
        for j in range(N):
            if not FW[i][j]:
                if FW[i][k] and FW[k][j]:
                    FW[i][j] = 1

result = 0
for node in range(N):
    cnt = 0
    for j in range(N):
        if node != j and FW[node][j]:
            cnt += 1
        if node != j and FW[j][node]:
            cnt += 1
    if cnt == N-1 :
        result += 1

print(result) 
