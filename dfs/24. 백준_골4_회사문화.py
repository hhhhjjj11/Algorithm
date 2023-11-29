# 정리
"""
dfs를 여러번돌리는게아니라 한번 돌려서 폭포수처럼 중간에 쌓여있는거 쫙~
"""
# 풀이
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().strip().split())
li = list(map(int,sys.stdin.readline().strip().split()))

g = [[] for i in range(n+1)]

for i in range(n):
    low = i+1
    high = li[i]
    if li[i] == -1:
        continue
    g[high].append(low)

record =[0]*(n+1)

def dfs(V, sum):
    record[V] += sum
    if len(g[V]) == 0:
        return
    for nextmember in g[V]:
        dfs(nextmember, sum+temp[nextmember])

temp = [0]*(n+1)
for _ in range(m):
    member, VALUE = map(int, sys.stdin.readline().strip().split())
    temp[member] += VALUE

# for i in range(1,n+1):
#     member, VALUE = i, temp[i]
#     dfs(member)

dfs(1,0)

for i in range(1,n+1):
    print(record[i], end= ' ')