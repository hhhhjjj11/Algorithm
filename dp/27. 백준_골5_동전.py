import sys

T = int(input())
results = []
for tc in range(T):
    N = int(input())
    li = list(map(int,sys.stdin.readline().strip().split()))
    M = int(input())

    dp=[0]*(M+1)

    for i in range(N):
        coin = li[i]
        for j in range(1, M+1): # 0 부터하면 18줄에서 걸려서 dp[0]=1이 됨.
            if dp[j]:
                if j+coin<=M:
                    dp[j+coin] += dp[j]
            if (j+coin)%coin == 0:
                dp[j]+=1
    results.append(dp[M])

for res in results:
    print(res)