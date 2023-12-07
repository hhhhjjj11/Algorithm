# 정리
"""
임시리스트 알았고. 
j+w, j-w 알았음. 근데 w-j는 몰랐다.
"""
# 풀이
import sys

N = int(input())
weight = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
ball = list(map(int,sys.stdin.readline().strip().split()))

dp = [0]*(40001)

for i in range(N):
    w = weight[i]
    temp = [w]
    for j in range(1, 40000):
        if dp[j]:
            if j+w <=40000:
                temp.append(j+w)
            if j-w >0:
                temp.append(j-w)
            if w-j>0:               # 이 부분을 놓침. 이 부분이 존나 빡세네
                temp.append(w-j)
    for t in temp:
        dp[t] = 1

res = []
for i in range(M):
    b = ball[i]
    if dp[b]:
        res.append('Y')
        continue
    res.append('N')

for r in res:
    print(r, end=' ')