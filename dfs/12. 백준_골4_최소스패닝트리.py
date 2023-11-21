import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split())

g  ={}
heap = [[0,1]]

for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    if a in g:
        g[a].append([c,b])
    else:
        g[a] = [[c,b]]
    if b in g:
        g[b].append([c,a])
    else:
        g[b] = [[c,a]]

ans = 0
visited = set()

cnt = 0

while heap:
    # print('heap',heap)
    weight, node = heapq.heappop(heap)  # 이미 여기서 제일 작은 값이 나온거임.
    # print('sdfs', weight, node)
    if cnt == V:
        break

    if not node in visited:
        visited.add(node)
        cnt += 1
        ans += weight
        # print('sdfsd', g[node])
        for i in g[node]:
            if not i[1] in visited:
                heapq.heappush(heap, i)

print(ans)