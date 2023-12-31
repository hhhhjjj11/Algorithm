# 정리
"""
DP문제임

증명 :
1,2,3,4 ~ N 까지잇다하자.
임의의 카드 하나를 생각하자. 
1을 생각하면, 1은 2~N 의 선물을 받을수있다.(N-1가지)
1이 2를 받았다고 하면
남은 사람 : 2,3,4, ... ,N
남은 선물 : 1,3,4, ... ,N
위 상황을 배분하는 경우의수는 
DP[N-1]에서 2가 1을 받는 경우를 더한 경우와 같다. 
왜냐하면 DP[N-1] 은 위 상황에서 2가 1을 받지 않는 경우의 수와 같기때문이다. (그렇게 하면 1을 2로 바꿔생각한거랑 일치)
(뭔말인지 알지? 대충썼다)
근데 2가 1을 받는 경우는 3~N이 3~N을 나눠갖는 경우의 수와 같으므로 DP[N-2]임.
그래서 DP[N-1] + DP[N-2] 임.

Thus, DP[N] = (N-1)*(DP[N-1]+DP[N-2])
"""

# 풀이
N = int(input())
mod = int(1e9)

dp = [0]*(N+1)

if N ==1:
    print(0)
    exit(0)
if N ==2 :
    print(1)
    exit(0)

if N==3:
    print(2)
    exit(0)

# n = 1
dp[1]=0
# n = 2
dp[2] = 1
dp[3] = 2 

for i in range(4,N+1):
    dp[i] = (i-1)*(dp[i-1] + dp[i-2])%mod

print(dp[N])

