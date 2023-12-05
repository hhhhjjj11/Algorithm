# 정리
"""
"""
# 풀이
import sys

N = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))

M_li = [0]*N    # M_li[i] = i까지 중에 최댓값의 인덱스

M = li[0]
Midx= 0
for i in range(N):
    if li[i] >=  M :
        M = li[i]
        Midx= i 
    M_li[i]= Midx

# print(M_li)
cnt1, cnt2 = 0,0
for wall in range(1,N):
    # 왼쪽의 최대 = 
    L,R = M_li[wall-1], M_li[-1] 
    if L == R:
        cnt1+=1
    else:
        if li[L] == li[R]:
            continue
        else:
            cnt2+=1

if cnt1 == cnt2:
    print('X')
elif cnt1>cnt2:
    print('R')
else:
    print('B')
    
    