# 정리
"""
이것도 코드로직이 복잡한게 아니라 문제 조건을 명제이용해서 해석 하는게 핵심이네
- 골드 1, 2쯤 되니까 명제를 이용하여 조건을 간단히 정리해야 시간,메모리 안에서 해결 가능한 문제들이 나온다..

문제 조건을 간단히 해도 만만치 않은 부분이 남아 있긴 함.
단순히 영역을 구분하는것 뿐만 아니라, 영역으로 포함되기만 하는 칸들까지 고려해줘야함.
-> 임시리스트를 활용해서 해결함.
"""

# 풀이
import sys

N, M = map(int, sys.stdin.readline().strip().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

char = ['N', 'W', 'E', 'S']
dir = [[-1,0], [0,-1], [0,1], [1,0]]

flag = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            
            flag += 1
            
            stack = []
            stack.append([i,j])
            visited[i][j] = flag
            temp = [[i,j]]

            while stack:
                i_now, j_now = stack.pop()
                idx = char.index(graph[i_now][j_now])
                i_next, j_next = i_now + dir[idx][0], j_now + dir[idx][1]
                temp.append([i_next,j_next])
                if visited[i_next][j_next] and visited[i_next][j_next] != flag:
                    flag -= 1
                    for a,b in temp:
                        visited[a][b] = flag
                    continue

                if not visited[i_next][j_next]:
                    visited[i_next][j_next] = flag
                    pass
                    stack.append([i_next,j_next])

print(flag)                    