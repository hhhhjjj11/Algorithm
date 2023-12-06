# 정리
"""
위상정렬 개념. + dp
1. 진입노드가 0인 노드들을 큐에넣고
2. 하나씩 꺼낸다음 꺼낸 노드들의 진출간선을 제거 -> 연결된 노드들의 진입노드가 하나씩 제거됨
3. 이제, 진입노드가 0인 노드들을 다시 큐에 넣고
4. 반복
5. 큐에넣는 순서 = 큐에서 뺀 순서 = 위상정렬

"""

# 풀이
import sys
from collections import deque

T = int(input())
results= []
for tc in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())
    D = list(map(int, sys.stdin.readline().strip().split())) # delay time 

    dp = [0]*N  # dp[i] = i번째 건물까지 완성시키는데 걸리는 시간. 말고

    check = [0]*N
    # dp 업데이트 타이밍?
    # 그리고. 노드가 를 끊을 때 dp 를 업데이트 해줘야 맞는 듯.

    O=[[] for _ in range(N)] # O[i] : i번 건물을 짓기 위해 선행되어야 하는 건물 넘버들.

    for _ in range(K):
        pre, later = map(int,sys.stdin.readline().strip().split())
        O[later-1].append(pre-1)
        
    W = int(input())

    # 위상 정렬
    Q = deque()
  
    while True:
        for i in range(1,N+1):
            if not check[i-1] and len(O[i-1]) ==0: # 진입 노드가 없으면 
                Q.append(i-1)

        if not Q:
            break

        while Q:
            node_from_Q = Q.popleft() # 큐에서꺼낸노드에 연결된 진출간선들을 싹다 없애야한다.
            dp[node_from_Q] += D[node_from_Q]
            check[node_from_Q] = 1
            for j in range(1,N+1):
                if node_from_Q in O[j-1]:
                    # 만약에 기존의 j번 노드의 시작시간이 진입노드의 시작시간 + 진입노드의 딜레이시간보다 작으면
                    # j번 노드는 시작못하고 그거 기다려야하니까 
                    if dp[j-1] < dp[node_from_Q]:
                        dp[j-1] = dp[node_from_Q]
                    O[j-1].remove(node_from_Q)
               
    results.append(dp[W-1])

for row in results:
    print(row)