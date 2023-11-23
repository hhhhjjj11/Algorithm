# 정리
"""
dfs 탐색, 깊이별로 visited체크, 카운트.

bottom - up / 

시행착오 - 위치로 하면 안되고 갯수 카운트로해야함. 좌표로하면 당연히안되지. 바보야

V 와 왼쪽가지들 갯수 를 분리 해서 세기.

"""

# 풀이
import sys
N = int(input())
tree = [[0,0]]*(N+1)

for _ in range(N):
    node, leftChild, rightChild = map(int,sys.stdin.readline().strip().split())
    tree[node] = [leftChild, rightChild]

g = [[0]*(N+1) for _ in range(N+1)]

def dfs(X, depthCnt, upCnt):    # 현재노드, 깊이, 오른쪽자식에게 전해줘야할 누적 갯수 값.
    print('시작', X, '/', depthCnt, upCnt)
    leftCount=0
    rightCount=0

    left, right = tree[X]

    # left 부터 탐색 해야 한다.
    if left != -1:
        leftCount = dfs(left, depthCnt+1, upCnt)
      
    if right != -1:
        rightCount = dfs(right, depthCnt+1, leftCount+1)

    g[depthCnt][upCnt+leftCount+1] = X
    print('종료', X, '/', leftCount, rightCount)
    return leftCount + rightCount + 1
        
dfs(1,1,0)

for row in g:
    print(row)