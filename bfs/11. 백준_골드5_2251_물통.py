# 정리
"""
3개 -> 두개만 알면 나머지는 구할 수 있기 때문에 두개만 가지고 visited랑 Q 돌린다!!

해보기 : 함수만들어서 재사용코드 활용하기

"""
# 풀이
import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().strip().split(" "))

Q = deque()
Q.append([0,0])

visited = [[0]*(B+1) for _ in range(A+1)]

    
while Q:

    A_now , B_now = Q.popleft()
    C_now = C - A_now - B_now

    # A -> B
    if A_now > (B-B_now):
        if not visited[A_now - (B-B_now)][B]:
            Q.append([A_now - (B-B_now), B])
            visited[A_now - (B-B_now)][B] = 1
    else:
        if not visited[0][B_now+A_now]:
            visited[0][B_now+A_now] = 1
            Q.append([0, B_now + A_now ])
    
    # A -> C
    if A_now > (C-C_now):
        if not visited[A_now-(C-C_now)][B_now]:
            Q.append([A_now-(C-C_now),B_now])
            visited[A_now-(C-C_now)][B_now] = 1
    else:
        if not visited[0][B_now]:
            Q.append([0,B_now])
            visited[0][B_now] = 1
    
    # B -> A
    if B_now > (A-A_now):
        if not visited[A][B_now -(A-A_now)]:
            Q.append([A,B_now -(A-A_now)])
            visited[A][B_now -(A-A_now)] = 1
    else:
        if not visited[A_now+B_now][0]:
            visited[A_now+B_now][0] = 1
            Q.append([A_now+B_now,0])

    # B -> C
    if B_now > C-C_now:
        if not visited[A_now][B_now-C+C_now]:
            Q.append([A_now,B_now-C+C_now])
            visited[A_now][B_now-C+C_now] = 1
    else:
        if not visited[A_now][0]:
            Q.append([A_now,0])
            visited[A_now][0] = 1
    # C -> A
    if C_now > A-A_now:
        if not visited[A][B_now]:
            Q.append([A,B_now])
            visited[A][B_now] = 1
    else:
        if not visited[A_now + C_now][B_now]:
            visited[A_now + C_now][B_now] = 1
            Q.append([A_now + C_now, B_now])
    # C -> B
    if C_now > B-B_now:
        if not visited[A_now][B]:
            Q.append([A_now,B])
            visited[A_now][B] =1
    else:
        if not visited[A_now][B_now + C_now]:
            Q.append([A_now, B_now+C_now])
            visited[A_now][B_now + C_now] =1

temp = []
for idx in range(B+1):
    if visited[0][idx] == 1:
        temp.append(C-idx)
temp.sort()
for i in range(len(temp)):
    print(temp[i], end=" ")