# 정리
"""
0. 우선, 어느점에서 시작해도 상관이 없음. (그럴 것 같긴한데 나중에 증명 해보기)
  - 예를들어, 1번 도시에서 시작하거나 2번에서 시작하거나 상관이없단 말.
  - 그래서 0번에서 시작하자
1. 우선, 출발점점과 남은점들에 대해, "시작점에서 시작하여 남은 점들을 도는 최소비용"을 저장해두고 재활용할거임.
  - 예를들어, 도시가 1~7까지 있고, 1->2->3 의 순서로 3에 와있다고 하자.
  - 만약에 3에서 시작하여 남은 도시들 {4, 5, 6, 7}을 모두 돌아 1로 돌아가는 최소비용을 이미 알고 있다면 계산을 이어나갈 필요가 없다.
2. 따라서, dp의 인자로 (시작점, 남은점들) 이 필요함.
  - 배열로는 남은점들을 표현하기 까다로움 
  - > 객체로 dp를 저장함.
3. DP[(now, remains)] = now에서 시작하고, remains의 노드들을 전부 순회하는데 필요한 최소비용.
4. DFS((now, remains)) = DP[(now, remains)]

* 편의를 위한 DP인자 바꿔서 표기: 
  - remains와 visited는 일대일대응임. (남은점들을 알면 항상 지나온 점들을 알고 반대의 경우도 마찬가지)
  - 따라서, 편의상 
    DP[(now, reamins)] 가 아니라 DP[(now, visited)]로 표기하고, 그렇게 되면,
    DP[(now, visited)] = "visited만큼 거쳐서 now까지 왔을때, now에서 시작하여 남은 점들을 전부 순회하는데 필요한 최소비용"을 의미.


5. 따라서, visited를 계속 DP에 저장해야함. 따라서 배열로 계속 저장하면 공간복잡도 안되고 비트마스킹을 이용한다.
=====================
비트마스킹 및 해설
- 링크참조 : https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-DP-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9-lso2bk58
- 아마 위 링크에서는 DP[(now,visited)] 에 관한 설명이 약간 잘못되어있는듯?
"""

# 풀이
import sys

N = int(input())
W = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

# DP[(now, visited)] = now에서 출발하고 visited말고 남은애들을 도는데 드는 최소비용
# DFS(now, visited) = DP[(now, visited)]

DP = {}

def DFS(now,visited):
    if visited == (1<<N) -1:
        # 전부다 방문
        if W[now][0]:
            # 사실 이부분은 DP로 만들어서 리턴해도되고 안그래도 됨.
            return W[now][0]
        else:   # 이 경우 now에서 0으로가는 길이 없는거임. 근데 정수형 리턴 안하면 에러나니까 답이 될리 없는 존나 큰 정수 리턴하는것으로하자.
            return int(1e9)
    
    if (now, visited) in DP:
        return DP[(now,visited)]

    DP[(now,visited)] = int(1e9)

    for next in range(N):
        # 길이 있고 방문한적이 없는 도시에 대해서만.
        if W[now][next] and not (visited & 1<<next):
            res = DFS(next, visited |1<<next ) + W[now][next]
            DP[(now,visited)] = min(DP[(now,visited)], res)

    return DP[(now,visited)]

print(DFS(0,1))