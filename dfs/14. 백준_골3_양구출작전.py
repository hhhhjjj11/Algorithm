# 정리
"""
- bottom up으로푼다.!!!

메모리초과 핵심이유 : 재귀 인자로 배열 X
- 재귀에 인자로 배열 계속넣으면 메모리 초과 나는듯 하다.
- 근데 bottom up으로 인자에 배열 안들어가게 하니까 낫긴 한데 여전히 메모리초과난다..

- 입력을 dic 말고 리스트로 해야하나?
- ㅅㅂ pypy3 말고 python으로 돌려야만 하는 문제였다. pypy3로 돌리면 메모리초과를 피할 수 없다고한다...;;
- 일반적인 경우는 dic보다 list가 더 나은듯.
- dic을 사용하는 것이 더 효율적인 경우는 좀 극단 적인 케이스 인듯. 배열길이가 억이 넘어가는경우??

"""
# 풀이
import sys
sys.setrecursionlimit(123458)

N = int(input())

g = {}
record = [0,0]
tree = [[] for _ in range(N+1)]

for s in range(2, N+1):     # 2부터 N-1개
    t,a,p = sys.stdin.readline().strip().split()
    a,p = int(a), int(p)
    record.append([t,a])
    if p in g:
        g[p].append(s)
    else:
        g[p] = [s]
    # tree[p].append(s)

    # if p==1:
    #     if 1 in g:
    #         g[1].append(s)
    #     else:
    #         g[1] = [s]
    # if p in g:
    #     g[p].append(s)
    # else:
    #     g[p] = [s]

# print(g)
# print(record)

# visited=[0]*(N+1)
def dfs(X):
    # visited[X] = 1
    
    res = 0

    if X in g:
    
        for adj in g[X]:
            # if not visited[adj]:
                # visited[adj]=1
            res += dfs(adj)
                # visited[adj]=0
    if X>1:
        str, val = record[X]
        if str == 'S':
            res += val
            # record[X][1] = 0
        else:   # 늑대면
            if record[X][1] >= res:
                res = 0
                # record[X][1] -= res
            else:
                res -= record[X][1]
                # record[X][1] = 0
    return res

print(dfs(1))