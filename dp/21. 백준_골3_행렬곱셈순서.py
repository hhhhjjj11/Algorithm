# 정리
"""
1. 2차원 dp 테이블, dp[i][j] = i번째행렬부터 j 번째 행렬까지의 곱에 필요한 연산 횟수
2. 이웃한 두개 부터 구해놓고 -> 3개 구해놓고 -> 4개 구해놓고 -> 5개구하고... -> 총 N개까지
3. 각 K개에서도 어떤식으로 곱하는것이 빠른지 알아야함, 칸막이로 구분만 해주면 그보다 하위의 계산은 이미 되어있으므로 활용
"""
# 풀이
import sys

N = int(input())
RC = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for K in range(2,N+1):  # 곱할 행렬 갯수 2부터 N까지..
    for start in range(N-K+1): # 시작행렬번호  0부터,, 
        # 범위넘어가면 다음탐색으로 넘어감
        if start + K-1 >= N:    
            break
        dp[start][start+K-1] = int(1e9)
        for div in range(1,K):  # 칸막이의 번호 : 앞 부터 1부터 시작.
            dp[start][start+K-1] = min(dp[start][start+K-1], dp[start][start+div-1] + dp[start+div][start+K-1] + RC[start][0]*RC[start+div-1][1]*RC[start+K-1][1])

print(dp[0][N-1])
