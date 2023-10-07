# 정리
"""
1. 무게가 1일때 -> 계속 갱신 됨.. -> 임시리스트화룡
2. dp를 건들면서 같은phase의 계산결과가 영향을 끼쳐서 오답을 발생시킴 -> 이전 db리스트를 따로 만들어서 활용

3. 꼼꼼한 오류 검토 - 입력무게가 아싸리 가방한계보다 큰 경우
"""
# 풀이
import sys

input = sys.stdin.readline
N, K = map(int,input().split())
bag = [0]*(K+1)

for _ in range(N):
    check = bag[:]
    W, V = map(int,input().split())
    for i in range(K+1):
        if i == 0:
            if W<=K and bag[W] < V:  # 물건하나가 가방전체한도보다 큰경우 체크. W<=K
                bag[W] = V
        else:
            if W+i <= K:
                if check[i] and bag[W+i] < bag[i] + V:
                    bag[W+i]= check[i]+V
print(max(bag))




# 생각해보자
