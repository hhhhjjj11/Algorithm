# 정리

# 풀이
import sys
sys.setrecursionlimit(10**5)
K = int(input())

for tc in range(K):
    V, E = map(int, sys.stdin.readline().strip().split())

    g = [[]for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int,sys.stdin.readline().strip().split())
        g[u].append(v)
        g[v].append(u)

    check = [0]*(V+1) # 미방문: 0 , 방문 및 인접 구분 : 1,2
    isNO = False
    def dfs(x): 
        global isNO    
        for adj in g[x]:
            if check[adj] and check[x] and check[adj] == check[x]:
                isNO = True
                break
            if not check[adj]:
                if check[x] == 1:
                    check[adj] =2
                    dfs(adj)
                elif check[x] ==2:
                    check[adj] = 1
                    dfs(adj)
        if isNO:
            return
    for start in range(1,V+1):
        if not check[start]:
            check[start] = 1
            dfs(start)

    if isNO:
        print("NO")
        continue
    print("YES")
