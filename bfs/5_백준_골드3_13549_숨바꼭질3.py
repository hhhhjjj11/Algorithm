# 정리
"""
1. 한번에 큐에 넣으면 안되고 시간은 따로 기억해야됨
2. 왜냐하면 일치하는 값이 나온다고해서 그 값이 최소란 보장이 없기때문에 
3. N == K 라고 끝내면 안되고 큐를 전부 다 돌린다음에 결과를 봐야함.
4. 다른말로, 큐의 뒤에있는 데이터에서 최소가 나올 수도 있다 이말임
- 이 부분에 대해서는 좀 더 생각해 볼것.
- 우선순위큐.. 
- 각각의 거리(간선의 개수/ 차원..? / 깊이..?)
- 각각의 같은 레벨에서 순간이동을 전부 다 해봐야 함.
- 큐의 뒤에다가 넣으면 안됨 visited가 이미 먹히면 답없음 (좀더 정리하기)
- 우선순위 큐라고해서, appendleft해야함.
"""
# 풀이
import sys
from collections import deque

N,K = map(int, sys.stdin.readline().strip().split(" "))

if N >= K:
    print(N-K) 
    exit(0)

else:
    Q = deque([])
    Q.append(N)

    visited = [0]*100001

    time = [0] * 100001
    while Q:
        now = Q.popleft()

        next = now*2
        # 이 조건이 존나 핵심인데.. 정리가 필요하다.
        if 0<=next <= 100000 and visited[next] and time[next]> time[now]:
            time[next] = time[now]

        if 0<= next <=100000 and not visited[next]:
            visited[next] = 1
            time[next] = time[now]
            Q.appendleft(next)
            
        next = now+1
        if 0<= next <= 100000 and not visited[next]:
            visited[next] = 1
            time[next] = time[now] +1
            Q.append(next)

        next = now-1
        if 0<=next <=100000 and not visited[next]:
            visited[next] = 1
            time[next] = time[now] +1
            Q.append(next)

    print(time[K])