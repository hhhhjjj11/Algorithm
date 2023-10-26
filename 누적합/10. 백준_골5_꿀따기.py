# 정리
"""
조금 생각해서 케이스를 대폭 줄이는 문제.

1. 조금만 생각해보면 케이스를 손쉽게 추릴 수 있음.
2. 모든 경우는 벌벌꿀 / 벌꿀벌/ 꿀벌벌 의 경우로 생각할 수 있는데, 
벌벌꿀과 꿀벌벌은 모두 벌들의 위치에 관계없이 항상 꿀통이 양쪽 끝에 놓여있을때가 최대임.
3. 또, 벌들 중에 한 마리는 끝에 붙어있을 때가 최대임.
따라서, 벌통과 벌을 양끝에 놓고 생각하면 됨.
4. 또, 꿀벌꿀의 경우 벌들이 양끝에 있을때가 무조건 최대.
3. 여기에 누적합 개념을 추가시켜서. 세번 반복문을 돌리면 되겠다.
"""
# 풀이
import sys
N = int(input())

li = list(map(int, sys.stdin.readline().strip().split()))

S = [0]*N
S[0] = li[0]

for i in range(1, N):
    S[i] = S[i-1] + li[i]

result = 0
for i in range(1,N-1):
    sum = S[N-1] - li[0] - li[i] + S[N-1] - S[i]  # 벌 -- 꿀 
    sum2 = S[N-1] - li[N-1] - li[i] + S[i-1]    # 꿀 -- 벌
    result = max(result, sum, sum2)

for i in range(1, N-1):
    sum3 = S[i] - li[0] + S[N-2] - S[i-1] 
    result = max(result, sum3)

print(result)