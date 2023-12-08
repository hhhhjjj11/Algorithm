# 정리
"""
첫번째 풀이는 답은 맞긴한데 10%에서 시간초과가 난다.
시간제한이 1초라.. 힙써서 더 최적화 해야만 통과 되는듯

아이디어
- 힙하나로 쇼부가능.
[겹치는 속성 순으로 정렬해서 따짐(무게), 힙에는 가치순으로 정렬, 힙을 계속 쓸 수 있도록 하려면 풀이대로 해야한다...] 
1. heap에는 가방보다 가벼운 보석들을 가치순으로 정렬 (최대힙)
2. 그리고 가벼운 가방부터 무거운 가방순으로 따져나감. 
  - 이전 가방에서 담아둔 힙에 추가시키기만 하면됨.
  - 그렇게 하면 힙을 계속 쓸 수 있음.
"""

# 풀이2 모범답안
import sys, heapq

N, K = map(int, sys.stdin.readline().strip().split())

gems = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

bags.sort()     # 오름차순
gems.sort(reverse=True)  # 무게기준 내림차순.

heap = []
res = 0
for i in range(K):
    bag = bags[i]
    # bag보다 가벼운 
    while gems and gems[-1][0] <= bag :
        heapq.heappush(heap, -gems.pop()[1])    # 가치를 넣음
    
    if heap:
        res += (-heapq.heappop(heap))

print(res)



# # 풀이1
# import sys, bisect

# N, K = map(int, sys.stdin.readline().strip().split())

# gems = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# bags = [int(input()) for _ in range(K)]
# visited = [0]*K
# # print(gems)

# # 가치가 높은 순으로 정렬
# gems.sort(key=lambda x:x[1], reverse=True)
# # print(gems)
# # 가방도 용량순으로 정렬
# bags.sort()
# # print('bag',bags)
# res = 0
# for i in range(N):
#     # 각 보석의 무게에 대하여 가장 가까운 가방을 찾는다.
#     W,V = gems[i]

#     index = bisect.bisect_left(bags, W)
#     if index >= K:
#         continue
#     find = True
#     while visited[index]:
#         index += 1
#         if index >= K:
#             find = False
#             break
        
#     if find:
#         visited[index] = 1
#         res += V 

# print(res)