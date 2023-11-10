# 정리
"""
시그마 등비합 이용한 것 밖에 생각이안나 dp테이블을 어케쓰는거야..

dp

arr[i][j] = a 3개와 z 2개로 만들 수 있는 단어 개수 

= 첫글자가 a인 경우 + 첫글자가 z인 경우
이때 첫글자가 a인 경우의수 = 2개 2개로 만들 수 있는 모든 경우의수
첫글자가 z인 경우의수 = 3개 1개로 만들 수 있는 모든 경우의수

따라서
= 2개2개로 만들 수 있는 모든 경우의 수 + 3개1개로 만들 수 있는 모든 경우의 수

"""
# 풀이
import sys

N, M, K = map(int,input().split()) # N : a갯수

dp = [[1]*(M+1) for _ in range(N+1)]  # dp[i][j] : a i 개와 z j 개로 만들 수 있는 단어의 수 / i: 0~N , j~0~M

# 0행은 전부 1이고 0열또한 전부 1

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if K > dp[N][M]:
    print(-1)
    exit(0)

result = ""

flag = dp[N-1][M] # 이는 맨 앞자리가 a인 경우의 수와 같음
# 따라서 이보다 K가 크면 사전순으로 그다음 번으로 넘어가야하므로 앞자리가 z가 되야한다.
# 그래서 

while True:
    
    if N == 0 or M == 0:
        result += 'a'*N
        result += 'z'*M
        break
    flag = dp[N-1][M]   # 약간 기준의 되는 의미..

    if K > flag:
        result += 'z'
        K -= flag  
        M -= 1
        continue
    
    result += 'a'
    N -= 1
    
print(result)