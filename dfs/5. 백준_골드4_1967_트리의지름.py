# 정리
"""
나는 bottom up 으로 잘 풀었다.
검색해보니까 문제 특성상 원하는 경우는 리프노드에서 리프노드까지의 거리만 구하면 된다는 점을 이용해서 
dfs로 푼 경우도 있었다.
시간은 걍 비슷한것같다.
"""
# 풀이
import sys
sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline().strip())
g = [[] for _ in range(n+1)]
dp = [[-1,0] for _ in range(n+1)] # 1~n 사용 # dp[k][0], dp[k][1] = k번 노드의 가장큰 끝까지값, 2번째로 큰 끝까지값.

for _ in range(n-1):
    pr, ch, l = map(int, sys.stdin.readline().strip().split())
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
    
    dp[X][0] = 0 
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

print(res)

