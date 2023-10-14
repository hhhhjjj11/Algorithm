from random import randint
import random
# subprocess.call

# 예제 생성
def example():
    print('sdfsdf')
    n = randint(1,10)
    nums = []
    parent=[1]
    temp = []
    while len(nums)<n-2:
        p = random.choice(parent)
        ch = randint(2,n)
        l = randint(1,100)
        if not [p,ch] in temp:
            nums.append([p,ch,l])
        temp.append([p,ch])
        parent.append(p)
    print('n',n, 'nums',nums)
    return n, nums    

# 맞은 답
import sys
sys.setrecursionlimit(10**5)


def right_sol(n, nums):
    tree = [[] for _ in range(n+1)]
    # 양방향 연결 리스트로 저장
    # 루트 노드 1인 부모-자식 트리라 하더라도
    # 루트의 지름을 구하려면 임의의 노드에서
    # 부모-자식 상하 관계에 구애받지 않고
    # 모든 노드를 순회할 수 있어야하기때문.
    for parent,child,weight in nums:
        tree[parent].append((child, weight))
        tree[child].append((parent, weight))
        
    def DFS(node, cost):
        for adj_node, adj_w in tree[node]:
            cal_w = cost + adj_w
            if visited[adj_node] == -1:
                visited[adj_node] = cal_w
                DFS(adj_node, cal_w)
        
        return

    # 첫 번째 DFS로 지름의 양 끝점 중 하나 구하기(성질 증명은 검색)
    visited = [-1]*(n+1)
    visited[1] = 0

    DFS(1, 0)
    idx, tmp = 0, 0
    for i in range(1, len(visited)):
        if visited[i] > tmp:
            tmp = visited[i]
            idx = i

    # 두 번째 DFS로 나머지 트리의 지름 끝점 하나를 찾고 지름 구하기
    visited = [-1]*(n+1)
    visited[idx] = 0
    DFS(idx, 0)

    return max(visited)


# 틀린 답

def wrong_sol(n, nums):
    g = [[] for _ in range(n+1)]
    dp = [[-1,0] for _ in range(n+1)] # 1~n 사용 # dp[k][0], dp[k][1] = k번 노드의 가장큰 끝까지값, 2번째로 큰 끝까지값.

    for pr,ch,l in nums:
        g[pr].append([ch,l]) 


    # print('g',g)
    # bottom up 으로 풀면 될것같은데

    # dfs(X) = X노드에서 잎새노드까지의 거리중 가장 큰 값과 두번째로 큰 값을 담은 길이 2의 배열
    # 자식노드들의 (dfs(자식) + 자식노드까지의 거리) 중 가장 큰 값임.
    def dfs(X):
        # print('호출',X)
        if len(g[X]) == 0: # 자식이 없는 노드인경우. 즉, 잎새노드.
            # print('잎새', X)
            dp[X] = [0,0]
            return dp[X]
            
        if dp[X][0] != -1:
            return dp[X]
        
        for child in g[X]:
            
            ch, l = child

            A, B = dfs(ch)
            # print('child, A, l', child, A, l)
            if dp[X][1] == 0:
                dp[X][1] = A+l
            if dp[X][0] < A + l:
                dp[X][1] = dp[X][0]
                dp[X][0] = A + l
            elif dp[X][0] == A+l:
                dp[X][1] = A + l
            elif dp[X][0] > A + l > dp[X][1]:
                # print(X, A+l, '이 2번째차지')
                dp[X][1] = A + l
            
        return dp[X]

    dfs(1)

    # print('dp',dp)
    res = 0
    for m1,m2 in dp:
        if m1+m2 > res:
            res = m1+ m2
    print('답', res)
    return res




# 반례 출력
def check():
	n, nums = example()
	right = right_sol(n, nums)
	wrong = wrong_sol(n, nums)
	if right != wrong:
		print(n, nums)

		print("맞은 답:", right)
		print("틀린 답:", wrong)
		return
	else:
		check()

check()