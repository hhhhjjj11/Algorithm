# 정리
"""
1. heap을 이용한다. 이때 파이썬에서 제공하는 라이브러리는 기본적으로 최소힙임. 그래서 pop하면 트리에있는 애들 중에서 가장 작은 값이 나옴.
그리고 push해도 알아서 재배열해서 자기자리 찾아가게 되어있음.
  - 그리고 힙에 넣는 튜플 또는 배열의 첫번째 값을 기준으로 대소비교를 하므로 가중치를 먼저 넣고 두번째로 노드번호를 넣어야
  가중치 기준으로 정렬됨.
2. mst구하는 알고리즘 로직
  - 간단함. 현재 갖고 있는 노드들 중에서 가중치가 가장 작은 간선을 선택해 나감.
  - 그런데 주의. 연산양이 작으면 그냥 MST = set() 으로 해도 되지만, 연산량이 많은 경우 heap을 이용한다.
  - 이문제에서는 set으로 하면 시간초과나고, heapq를 이용해야 함.

  2.1. set을 이용한 수도코드

    V, E = 노드갯수, 간선갯수
    g = 연결노드를 표현한 dictionary , 입력받아서 완성한다.
    
    MST = set()
    visited = set()

    ans = 0

    while len(MST) < V:   MST에 노드갯수가 일치할때까지 가중치가 가장 작은 노드를 추가시킬 것임.
        W_min = 0
        node_min = 0
        for node in MST:    # mst집합에 들어있는 노드들의 인접노드들에 대하여 간선의 가중치가 최소가 되는 case를 찾는다.
            for li in g[node]:
                weight, adj_ndoe = g[node]
                if not adj_node in visited and W_min > weight:
                    W_min = weight
                    node_min = 0
        
        # 찾았으면 mst와 결과에 반영
        mst.add(node_min)
        ans += W_min
                    
    print(ans)

  
  2.2. 성능개선을 위한 heap사용

    import heapq

    ans = 0
    
    heap = [[0,1]] # 시작점을 넣는다.
    cnt = 0

    while heap:
        weight, node = heapq.heappop(heap)
        # heap은 MST집합이 아니라, 현재 트리의 인접노드들의 집합임.
        
        # 넣을때는 걍 여기서 검사하는게 더 빠른 것 같다.
        if node in visited:
            continue
            
        cnt += 1    # 하나 꺼냇다 -> mst집합에 노드 하나를 추가한것과 같음.
        
        if cnt == V:
            break
            
        for i in g[node]:
            weight, adj_node = i
            if not adj_node in visited: # 여기서 해도 되지만 위에서 하고 걍 여기서는 안하는게 낳은듯. 일단 적어둠.
                heapq.push(heap,i)          # 넣기만 하면 알아서 재배열 된다는 사실 기억하자.

"""
# 풀이

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