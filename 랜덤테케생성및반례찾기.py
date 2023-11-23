from random import randint
import random
# subprocess.call

# 예제 생성
def example():

    n = randint(0,10)
    while not n%2:
        n = randint(0,10)
    print(n)
    list = []
    SET = set()
    SET.add(1)
    isFull = False
    if n%2: # 짝수면은 한개남음 홀수면 딱떨어짐
        for i in range(1,n+1):
            A = randint(i+1,n)
            B = randint(i+1,n)
            while A in SET:
                A = randint(i+1,n)
                print('A',A)
            while B in SET or B==A:
                B = randint(i+1,n)
                print('B',B)

            list.append([i,A,B])
            SET.add(A)
            SET.add(B)
            
            if len(SET) == n:
                isFull = True
                break
            NUMBER = i+1
    
    for x in range(i+1,n+1):
        pass
        list.append([x,-1,-1])
    return n, list

# 맞은 답
import sys
sys.setrecursionlimit(10**5)
from collections import deque

def right_sol(n, list):

    n = int(sys.stdin.readline())
    tree = [[-1, -1, -1] for x in range(n+1)]
    for i in range(n):
        node, lc, rc = list[i]
        tree[node][1] = lc
        tree[node][2] = rc
        tree[lc][0] = n
        tree[rc][0] = n
    root = -1
    
    for i in range(1, n+1):
        if tree[i][0] == -1:
            root = i

    visit = [[-1, -1] for x in range(n+1)] # r: level, c: dist
    def bfs(root):
        maxdepth = 0
        queue = deque([root])
        visit[root][0] = 0
        while queue:
            node = queue.popleft()
            lc = tree[node][1]
            rc = tree[node][2]
            if lc != -1:
                if visit[lc][0] == -1:
                    visit[lc][0] = visit[node][0] + 1
                    maxdepth = max(visit[lc][0], maxdepth)
                    queue.append(lc)
            if rc!= -1:
                if visit[rc][0] == -1:
                    visit[rc][0] = visit[node][0] + 1
                    maxdepth = max(visit[rc][0], maxdepth)
                    queue.append(rc)
        return maxdepth

    global dist
    dist = 0
    def inorder_search(node):
        global dist
        if tree[node][1] != -1:
            inorder_search(tree[node][1])
        dist += 1
        visit[node][1] = dist

        if tree[node][2] != -1:
            inorder_search(tree[node][2])

    maxdepth = bfs(root)
    inorder_search(root)
    maxdist = 0
    minlevel = 1e10

    if n == 1:
        print(1)
        print(1)
        return 1,1
    else:
        for d in range(maxdepth+1):
            minval = 1e10
            maxval = 0
            for i in range(1, n + 1):
                if d == visit[i][0]:
                    minval = min(visit[i][1], minval)
                    maxval = max(visit[i][1], maxval)
            if maxdist < maxval-minval+1:
                minlevel = d+1
                maxdist = maxval-minval+1

        print(minlevel)
        print(maxdist)
        return minlevel, maxdist


# 틀린 답
import sys

def wrong_sol(N, list):

    tree = [[0,0] for _ in range(N+1)]

    for XX in range(N):
        node, leftChild, rightChild = list[XX]
        tree[node] = [leftChild, rightChild]

    g = {}

    def dfs(X, depthCnt, upCnt):    # 현재노드, 깊이, 오른쪽자식에게 전해줘야할 누적 갯수 값.
        # print('시작', X, '/', 'dep', depthCnt, 'V', upCnt)
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
        # print('종료', X, '/', 'left', leftCount,  'right', rightCount)
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

    # for row in g:
    #     print(row)

    # print(g)

    for deep in g:
        if ans2 <= max(g[deep]) - min(g[deep]) + 1:
            ans2 = max(g[deep]) - min(g[deep]) + 1
            if ans1 > deep:
                ans1 = deep

    print(ans1, ans2)
    return ans1, ans2

# 반례 출력
def check():
    n, list = example()
    right = right_sol(n, list)
    wrong = wrong_sol(n, list)

    if right != wrong:
        print(n, list)

        print("맞은 답:", right)
        print("틀린 답:", wrong)
        return
    else:
        print(n, list)
        check()

check()