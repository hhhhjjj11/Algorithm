# 정리
"""
i+v말구 i-v로 쓰면 좀 더 편함.
dp[0] = 1도 써줘야함 동전 하나만 쓰는 경우...

어떤식으로 계산하는건지 흐름 이해하기..
누적해나가기.
컴퓨터는 단순계산이 존나빠르네
"""
# 풀이
n, k = map(int,input().split())

dp = [0]*(k+1)
dp[0] = 1
for _ in range(n):
    v = int(input())
    for i in range(v,k+1):
        dp[i]+=dp[i-v]

print(dp[k])