from random import randint
# subprocess.call

# 예제 생성
def example():
    N = 5
    M = 5
    nums = []
    while len(nums)<M:
        a = randint(0,N-1)
        b = randint(0,N-1)
        if a !=b and [a,b] not in nums and [b,a] not in nums:
            nums.append([a,b])

    return N, M, nums    

# 맞은 답
import sys


def right_sol(n, m, nums):
    link = [[] for _ in range(n)]
    
    for a, b in nums:
        link[a].append(b)
        link[b].append(a)
        
    def dfs(v, d):
        if d == 4:
            return True
        for i in link[v]:
            if not visited[i]:
                visited[i] = True
                if dfs(i, d + 1):
                    return True
                visited[i] = False
        return False

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        if dfs(start, 0):
            return 1
        
    return 0


# 틀린 답

def wrong_sol(N, M, nums):
    g = [[] for _ in range(N)]

    for a,b in nums:
        g[a].append(b)
        g[b].append(a)

    for start in range(N):
        stack = []
        stack.append([start, 0])
        bt = [[start, 0]]
        visited = [0]*N
        visited[start] = 1

        while stack:
            
            now, depth = stack.pop()
            if not visited[now]:
                visited[now]=1
            temp = []
            for v,d in bt:
                if d>=depth and v != now:
                    visited[v] = 0
                    temp.append([v,d])
                if d> depth and v==now:
                    temp.append([v,d])
            for v,d in temp:
                bt.remove([v,d])

            if depth == 4:
                print("start", start)
                return 1
                exit(0)
            for friend in g[now]:
                if not visited[friend]:
                    stack.append([friend, depth+1])
                    visited[friend]=1
                    bt.append([friend,depth+1])
    
    return 0



# 반례 출력
def check():
	N,M,nums = example()
	right = right_sol(N,M,nums)
	wrong = wrong_sol(N,M,nums)
	if right != wrong:
		print(N,M,nums)

		print("맞은 답:", right)
		print("틀린 답:", wrong)
		return
	else:
		check()

check()