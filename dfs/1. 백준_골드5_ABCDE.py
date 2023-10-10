# 정리
"""
1. depth를 찾는 문제 -> 단순 탐색만 하면 되는 문제가아님
2. 순서도 중요함
예를들어. 1-2-3-4-5 로 들어있다고 치면 만약에 3부터 탐색할 경우 depth는 2가 최대임 
3. 위와 같은 그래프에서 어디가 연결의 끝인지 알 수 없음.
4. 따라서 각 노드에 대해서 dfs를 전부 돌려주어야함. 
5.
"""
# 풀이
import sys
N, M = map(int,sys.stdin.readline().strip().split())

g = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().strip().split())
    g[a].append(b)
    g[b].append(a)


for start in range(N):
    stack = []
    stack.append([start, 0])
    visited = [0]*N
    visited[start] = 1

    while stack:
    
        now, depth = stack.pop()
        if depth == 4:
            print(1)
            exit(0)
        for friend in g[now]:
            if not visited[friend]:
                stack.append([friend, depth+1])
            
        visited[now] = 1

print(0)