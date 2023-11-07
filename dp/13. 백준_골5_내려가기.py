# 정리
"""
풀이 외우기 약간 그리디 + dp인 느낌인건가?
"""
# 풀이
import sys

N = int(input())

g = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

a1,b1,c1= g[0]

M = [0,0,0]
m = [0,0,0]

for i in range(N):
    a,b,c = g[i]
    M = [a+max(M[0],M[1]), b+max(M), c+max(M[1],M[2])]
    m = [a+min(m[0],m[1]), b+min(m), c+min(m[1],m[2])]

print(max(M), min(m))