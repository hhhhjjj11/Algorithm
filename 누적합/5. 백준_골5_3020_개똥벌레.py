# 정리
"""
구간에 해당하는 수를 세는거를 누적합 아이디어를 적용해서 쉽게 계산한다는거...
골드5이지만 나는 생각도 못했다;;

"""
# 풀이
import sys

N, H = map(int,sys.stdin.readline().strip().split())    # 0,1,2,3,4,...,H-1

up = [0]*H
down = [0]*H

for i in range(N):
    if i%2 == 0:
        # 석순
        h = int(input())
        down[h-1] += 1
    else:
        # 종유석
        h = int(input())
        up[h-1] += 1


for i in range(H-2, -1,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min = 99999999
count = 0
for i in range(H):
    # 장애물 세기
    if min > up[i] + down[H-1-i]:
        min = up[i] + down[H-1-i]
        count = 1
    elif min == up[i] + down[H-1-i]:
        count += 1

print(min, count)