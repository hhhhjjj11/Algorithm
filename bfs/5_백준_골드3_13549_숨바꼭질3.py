# 정리
"""
우선순위 큐 
- 먼저들어오는 데이터가 먼저나가는게 아니라, 우선 순위가 높은 데이터가 먼저 나가는 형태의 자료구조

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



# 다익스트라 -> 정답을 계속 해서 갱신 해야함 
# 다익스트라라는 것을 어떻게 판별 하는가

# 언니위치 N 동생위치 K
# 순간이동은 가중 현재위치에서 각각의 노드가 가중치가 다르다!!!
# 가중치가 다르기 때문에 

# 언니 위치에서 bfs 로 찾아야한다. 한칸 뒤 / 앞 / 두배
# 질문. 왜 dfs는아니지? 어차피 다 찾아야하면 dfs여도 상관 없는거 아닌가
# 이때 가중치가 다르다. 한칸 뒤 / 앞은 +1 인 반면, 두 배는 +0임
# 우선, 다익스트라 (해당 값이 나온다고 최소가 아니라 뒤에서 최소가 나올 수도 있는 경우)이기 때문에
# 그리고 
# 정답 체크를 위한 리스트를 따로 만들어서 관리 해줘야함. (언제 갱신될지 모른다.)
# 질문. 그러면 기본적으로 다익스트라는 모든 탐색이 끝날때까지 기다리긴 해야하나?
# 그렇기 때문에
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
        # "정답갱신"이 일어날 수 있는 부분은 -> visited 여부가 의미가 없음. 이거는 특히 이 문제가 노드까지 가는 길이 정해진게 아니라
        # 이동방법만 제시하고있고 해당 이동 방법들을 가지고 노드까지 가는 경로가 무수히 많을 수 있기 때문인 듯. 
        # 정답 갱신이 일어날 수 있는 부분은 -> 가중치의 역전이 있는 *2로 이동하는 경우임.
        # visied
        if 0<=next <= 100000 and time[next]> time[now]:
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