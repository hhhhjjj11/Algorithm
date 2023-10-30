# 정리
"""

"""

# 풀이
import sys
N, M =  map(int, input().split())
g =[list(map(int ,sys.stdin.readline().strip().split())) for _ in range(N)]

S = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + g[i-1][j-1]

MAX = -10000000000
for si in range(1,N+1):
    for sj in range(1, M+1):
        for ei in range(si, N+1):
            for ej in range(sj, M+1):
                V = S[ei][ej] + S[si-1][sj-1] - S[si-1][ej] - S[ei][sj-1]
                if MAX < V : 
                    MAX = V

print(MAX)