# 정리
"""
오.. 아이디어가 신박하다
핵심 : 일단 0그룹들의 갯수를 저장해놨다가 1하고 인접한 그룹이 뭔지만 체크하고 더해주면 됨. 

일일이 dfs로 셀 필요가 없다. 세놨다가 더하기만하면 된다..
"""
# 풀이
import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().strip().split())

g = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

# print(g)

def dfs(i,j):
    check[i][j] =flag
    X = 1
    for p in range(4):
        i_next, j_next = i+di[p] , j+dj[p]
        if 0<=i_next<N and 0<=j_next<M and not g[i_next][j_next] and not check[i_next][j_next]:
            X += dfs(i_next, j_next)
    return X

check = [[0]*M for _ in range(N)]
flag = 0
dic = {}
for i in range(N):
    for j in range(M):
        if not g[i][j] and not check[i][j]:
            flag+=1
            dic[flag] = dfs(i,j) 

# print(dic)
# print(check)
# print(g)

res = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            temp = set()
            for q in range(4):
                i_adj , j_adj = i+di[q], j+dj[q]
                if 0<=i_adj<N and 0<=j_adj<M and not g[i_adj][j_adj]:   # 주변이 0이면
                    
                    temp.add(check[i_adj][j_adj])
            
            for groupnum in temp:
                res[i][j] += dic[groupnum]      # 여기서 g[i][j] += dic[groupnum]
            res[i][j] += 1                      # g[i][j] += 1
            res[i][j] %= 10                     # g[i][j] %= 10 하면 안됨!!!!
                                                # 왜냐. 0으로 바뀌면 바로에러남
for row in res:
    print(''.join(map(str,row)))