# 정리
"""
bottom up 인데
DP[i][j] 못쓴다. (욕심쟁이 판다랑 비교.)

"어떤 경로로 왔든간에, 다음으로 펼쳐질 경우의 수가 같을 때. 조금이라도 달라지면 장담못함."

DP를 쓸 수 있는 경우
핵심: 한 번 밟고 계산 한적이 있으면 -> 그 결과 값이 확실할때임.
그렇게 되려면??? -> 어떤 경로로 (i,j)까지 왔든간에 관계없이, 다음으로 따져야할 경우의 수가 같을때임.
그렇게 되면 -> 이미 모든 경우를 따져본적이 있으므로 충분하게 됨(모든 과정은 중복되므로 더 계산 필요X).
반대로, 이번에는 따져야할 경우가 달라진다면?? DP를 쓰면 안되는거임.

그러므로, DP[i][j]를 재활용하려면 (i,j)까지 이렇게 왔든 저렇게 왔든, 그 다음에 밟을 수 있는 땅이 같아야만함!!!!

그런데, 욕심쟁이판다에서는 그게 맞음. 왜냐?. 현재땅보다 값이 큰 경우로만 이동이 가능하기 때문에, 왼쪽에서 왔든 오른쪽에서 왔든
상관이 없이, 다음으로 갈 수 있는 곳은 현재칸보다 값이 큰곳이기때문에, 어디서 왔든 다음으로 따져주어야할 경우의 수가 동일함.

하지만, 이 문제의 경우 다르다!!
왼쪽에서 온경우는 1.오른쪽 2.아래로 갈 수 있고, 오른쪽에서 온경우 1.왼쪽 2.아래로 갈 수 있음.


그래 ! DP[i][j] 로 하면 안된다는 거 알게써!
뭐 방법 없을까?

이렇게 하면 됨. (i,j,왼쪽에서옴) / (i,j,오른쪽에서옴) / (i,j,위에서내려옴) 하면 왼쪽에서왔으면 항상 따져야될 경우가 같고 오른쪽에서 왓어도 마찬가지기때문.
위에서내려온 경우도 따로 분리해야한다... 좀 더 깊이 생각해보기.

풀이2로 하면 답은 맞음.(정답풀이랑 랜덤테케돌려봄) 근데 시간초과 메모리 초과 난다. dp를 세 개의 케이스로 구분하여 저장하기 때문에 사실상 메모이제이션 효과가 떨어짐.

오케이 삽질 잘했고. 
DPㄱㄱ
"""
# 풀이2
import sys
sys.setrecursionlimit(int(1e6))
N, M = map(int,sys.stdin.readline().strip().split())
g = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
DP = [[[-int(1e9), -int(1e9), -int(1e9)] for _1 in range(M)] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# DP[i][j] = i,j에서 N-1,M-1까지 가치최대

# 왼, 오, 아래
di = [0,0,1]
dj = [-1,1,0]

def DFS(i,j, dir): 
    # print(i,j,'/',dir)
    if i==N-1 and j==M-1:
        return g[N-1][M-1]
    
    if DP[i][j][dir] > -int(1e9):
        return DP[i][j][dir]

    MAX = -int(1e9)
    
    for k in range(3):
        i_next, j_next = i + di[k],j + dj[k]
        if 0<=i_next<N and 0<=j_next<M and not visited[i_next][j_next]:
            visited[i_next][j_next] = 1
            res = DFS(i_next,j_next,k)
            if MAX < res + g[i][j]:
                MAX = res + g[i][j]
            visited[i_next][j_next] = 0
    # print(i,j,'/',dir,'종료')
    
    DP[i][j][dir] = MAX
    return MAX

visited[0][0] =1
DFS(0,0,1)
DFS(0,0,2)
print(max(DP[0][0]))