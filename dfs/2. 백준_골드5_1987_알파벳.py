# 정리
"""
1. 이 문제의 경우 visited를 따로 쓸 필요가 없다!!
visited를 쓰면 시간초과나고 안쓰니까 통과한다..

2. 알파벳을 리스트를 쓰지말고 ord메서드를 이용해서 인덱스로 이용한다...
리스트보다 그편이 시간절약에 훨씬 효과적.
"""
# 풀이

import sys

R, C = map(int, sys.stdin.readline().strip().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

record = [0]*26

dx = [0,0,1,-1]
dy = [1,-1,0,0]

record[ord(graph[0][0].lower())-ord('a')] = 1

max =  0
def dfs(i,j, count):
    global max
    if count>max:
        max = count

    for p in range(4):
        
        i_next, j_next = i+dx[p], j+dy[p]

        if 0<=i_next<R and 0<=j_next<C and not record[ord(graph[i_next][j_next].lower())-ord('a')]:
            
            record[ord(graph[i_next][j_next].lower())-ord('a')] = 1       
            dfs(i_next,j_next,  count+1)
            record[ord(graph[i_next][j_next].lower())-ord('a')] = 0

dfs(0,0, 1)
print(max)