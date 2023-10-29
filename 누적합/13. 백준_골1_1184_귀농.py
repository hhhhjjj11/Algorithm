# 정리
"""
가닥은 잘잡았는데 교차점 기준으로 반복문 돌리는것이 훨씬 따져야할 가짓수가 적다는 점 알고가자.
(얼마나 적은지는 공부필요)
================================================================================
1. 케이스는 두 가지 
 - case1 : 좌상 + 우하
 - case2 : 좌하 + 우상

2. 모든 경우의 수  = (좌상+우하로 붙는 모든 경우) U (좌하+우상으로 붙는 모든 경우)
그리고, 가능한 모든 사각형 집합을 {R1, R2, R3, ... , Ri}라 할 때,
좌상+우하로 붙는 모든 경우 = (R1이 좌상인경우) U (R2가 좌상인경우) U ... U (Ri가 좌상인경우)
(pf) 좌상+우하로 붙는 모든 경우는 우변의 결과에 항상 포함됨.
마찬가지로, 좌하+우상으로 붙는 모든 경우 = (R1이좌하인경우) U (R2가 좌하) U ... U (Ri가 좌하)

결과적으로, 모든 경우의 수 = (R1이 좌상 또는 좌하인경우) U (R2가 좌상 또는 좌하인경우) U ... U (Ri가 좌상 또는 좌하인 경우)

따라서 각 Rk (1<=k<=i)에 대해 
우상영역과 우하 영역으로 나누고, 두 영역에서 Ri와 값이 같은 경우를 찾아서 세준다. n=50이므로 완탐쌉가능

3. 이제 풀어보자 .. 쳐맞는계획인지 진짜 계획인지.

=======> 일단 가닥은 잘 잡았는데. 그래도 시간초과가 난다. 시간을 더 줄일 수 있는 방법이 있었다..
핵심: 경계포인트를 기준으로 잡고 계산한다.

우선 경계포인트 divi,divy를 기준으로 양쪽을 나눠생각하는게 나음 그러면 2중 반복문 하위에서 계산
근데 나는 네모를 먼저 생각해서 4중반복문을 돌리고 각각에서 탐색함

"""
"""
# 나의 첫 풀이 : 답은 맞는듯. 근데 시간초과.
import sys

N = int(input())

g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

# S[i][j] = (0,0) 부터 (i,j) 까지의 수익

S= [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j]= S[i-1][j] + S[i][j-1] - S[i-1][j-1] + g[i-1][j-1]

# print("=============")
# for row in S:
#     print(row)
# print("=============")
answer = 0

for si in range(1,N+1):
    for sj in range(1,N+1):
        for ei in range(si, N+1):
            for ej in range(sj, N+1):
                # print("===============================")
                V = S[ei][ej] + S[si-1][sj-1] - S[ei][sj-1] - S[si-1][ej]
                # 우상 탐색
                # print("si,sj,ei,ej", si,sj,ei,ej)
                # print("v", V)
                # print("------------------------------")
                # print("우상 탐색 시작")
                for i in range(1,si):
                    for j in range(ej+1, N+1):
                        temp = S[si-1][j] + S[i-1][ej] - S[i-1][j] - S[si-1][ej]
                        # print("i, j", i, j)
                        # print('temp', temp)
                        if V == temp:
                            # print('같음')
                            answer += 1
                        # print('---')

                # print("우하 탐색 시작")
                # 우하 탐색
                for i in range(ei+1, N+1):
                    for j in range(ej+1, N+1):
                        temp = S[i][j] + S[ei][ej] - S[ei][j] - S[i][ej]
                        # print("i, j", i, j)
                        # print('temp', temp)
                        if V == temp:
                            # print('같음')
                            answer += 1

print(answer)
"""

import sys
from collections import defaultdict


N = int(input())

g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

# S[i][j] = (0,0) 부터 (i,j) 까지의 수익

S= [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j]= S[i-1][j] + S[i][j-1] - S[i-1][j-1] + g[i-1][j-1]

# print("=============")
# for row in S:
#     print(row)
# print("=============")

answer = 0

def Calculator(si,sj,ei,ej):
    return S[ei][ej] + S[si][sj] - S[si][ej] - S[ei][sj]

for divI in range(1, N):
    for divJ in range(N):
        dd = defaultdict(int)
        # 좌상 + 우하
        # 좌상.
        for i in range(divI):
            for j in range(divJ):
                V = S[divI][divJ] + S[i][j] - S[i][divJ] - S[divI][j]
                dd[V] += 1
        # 우하
        for i in range(divI+1, N+1):
            for j in range(divJ+1, N+1):
                V = S[i][j] + S[divI][divJ] - S[divI][j] - S[i][divJ]
                answer += dd[V]
        
        # 좌하 + 우상
        # 좌하
        dd = defaultdict(int)
        for i in range(divI+1, N+1):
            for j in range(divJ):
                V = Calculator(divI,j, i,divJ)
                dd[V] += 1
        # 우상
        for i in range(divI):
            for j in range(divJ+1,N+1):
                V = Calculator(i,divJ,divI,j)
                answer += dd[V]

print(answer)