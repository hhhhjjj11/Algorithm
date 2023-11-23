# 정리
"""
dfs 탐색, 깊이별로 visited체크, 카운트.

bottom - up / 

시행착오 - 위치로 하면 안되고 갯수 카운트로해야함. 좌표로하면 당연히안되지. 바보야

V 와 왼쪽가지들 갯수 를 분리 해서 세기.

- 메모리관련. 배열 int 한칸에 4byte. 따라서 10000 * 10000 2차원배열 -> 4 x 10**8 -> 400MB ;;
========================================================================================
피지컬로 풀긴했는데 중위순회를 이용하는 문제임. 중위순회로 다시 풀기.
"""
# 풀이2 - 중위순회


# 풀이1
import sys
N = int(input())
tree = [[0,0] for _ in range(N+1)]

for _ in range(N):
    node, leftChild, rightChild = map(int,sys.stdin.readline().strip().split())
    tree[node] = [leftChild, rightChild]

g = {}

def dfs(X, depthCnt, upCnt):    # 현재노드, 깊이, 오른쪽자식에게 전해줘야할 누적 갯수 값.
    leftCount=0
    rightCount=0

    left, right = tree[X]

    # left 부터 탐색 해야 한다.
    if left != -1:
        leftCount = dfs(left, depthCnt+1, upCnt)
      
    if right != -1:
        rightCount = dfs(right, depthCnt+1, leftCount+upCnt+1)
    
    if depthCnt in g:
        g[depthCnt].append(upCnt+leftCount+1)
    else:
        g[depthCnt] = [upCnt+leftCount+1]
    return leftCount + rightCount + 1

# 루트 노드 찾기.
for X1 in range(1, N+1):
    isRoot = True
    for node in range(1, N+1):
        if X1 in tree[node]:
            isRoot = False
            break
    if isRoot:
        root = X1
        break
            
dfs(root,1,0)

ans1 = 10**10
ans2 = 0

for deep in g:
    if ans2< max(g[deep]) - min(g[deep]) + 1:
        ans2 = max(g[deep]) - min(g[deep]) + 1
        ans1 = deep
    elif ans2 == max(g[deep]) - min(g[deep]) + 1 and ans1 > deep:
        ans1 = deep

print(ans1, ans2)