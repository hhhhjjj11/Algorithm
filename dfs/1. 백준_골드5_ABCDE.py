# 정리
"""
스택은 이제 놓아주자..
ㅅㅂ 코테부터 풀어야할거 아니야 이 싀발
임시 리스트를 만들어서 depth와 함께 표시하여서 백트래킹에 활용할 수 있을 것 같긴한데.
그렇다고 하더라도 재귀로 하는게 더 효율적인 듯 하다.(잘모르지만)
이 문제만 그렇게 풀고 걍 재귀로 하자..

1. depth를 찾는 문제 -> 단순 탐색만 하면 되는 문제가아님
2. 순서도 중요함
예를들어. 1-2-3-4-5 로 들어있다고 치면 만약에 3부터 탐색할 경우 depth는 2가 최대임 
3. 위와 같은 그래프에서 어디가 연결의 끝인지 알 수 없음.
4. 따라서 각 노드에 대해서 dfs를 전부 돌려주어야함.
5. 스택으로는 백트래킹 적용이 안됨
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
    bt = [[start, 0]]
    visited = [0]*N
    visited[start] = 1

    while stack:
        
        now, depth = stack.pop()
        if not visited[now]:
            visited[now]=1
        temp = []
        for v,d in bt:
            if d>=depth and v != now:
                visited[v] = 0
                temp.append([v,d])
            if d> depth and v==now:
                temp.append([v,d])
        for v,d in temp:
            bt.remove([v,d])

        if depth == 4:
            print("start", start)
            print(1)
            exit(0)
        for friend in g[now]:
            if not visited[friend]:
                stack.append([friend, depth+1])
                visited[friend]=1
                bt.append([friend,depth+1])
 

print(0)