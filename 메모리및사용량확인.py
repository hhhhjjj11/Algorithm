import tracemalloc
import time
import sys

tracemalloc.start()
st = time.time()
mod = 1000000007




sys.setrecursionlimit(10000)

N = int(input())

g = {}
record = [0,0]
for s in range(2, N+1): # 2부터 N-1개
    t,a,p = sys.stdin.readline().strip().split()
    a,p=int(a), int(p)
    record.append([t,a])
    if s in g:
        g[s].append(p)

    else:
        g[s] = [p]
    # if p==1:
    #     if 1 in g:
    #         g[1].append(s)
    #     else:
    #         g[1] = [s]
    if p in g:
        g[p].append(s)
    else:
        g[p] = [s]

# print(g)
# print(record)
res = 0
visited=[0]*(N+1)
def dfs(X,li):
    visited[X] = 1
    is_leaf = True
    for adj in g[X]:
        if not visited[adj]:
            is_leaf= False
            visited[adj]=1
            dfs(adj,li+[adj])
            visited[adj]=0
    if is_leaf:
        # print('리프노드 : ', X, li)
        global res
        temp = 0
        for idx in range(len(li)-1,-1,-1):
            node = li[idx]
            if record[node][0] == 'S': # 양
                temp += record[node][1]
                record[node][1] = 0
            else:   # 늑대
                # 늑대가 현자깨지 값보다 크면 0
                if record[node][1] >= temp:
                    temp = 0
                    record[node][1] -= temp
                else:
                    temp -= record[node][1]
                    record[node][1] = 0 
        # print('리프노드 : ', X, '  더하는값', temp)

        res += temp  
        # print(res) 

dfs(1, [])

print(res)
# 코드 끝
# 실행 시간: 206.12s
# 메모리 사용량: 약 31200 KB + 110KB

cur_mem, peak_mem = tracemalloc.get_traced_memory()

print(f'Execution: {time.time() - st : .3f}s')
print(f'Memory: {peak_mem/1024. : .3f}KB')
tracemalloc.stop()