# 정리
"""
명제를 이용한 풀이 축소
1. 위부터 돌리고 dfs도 오른쪽 위부터 돌린다.
  - 오른쪽 위부터 탐색하고 도달하면 끝내는게 핵심임 
  - 왜냐하면 위에서부터 이제 파이프를 뽑아볼건데, 파이프가 한번 연결되면 아래에있는애들은 그 파이프를 가로지를 수 없기때문에,
    어떻게든 최대한 많이 공간을 다음애들한테 넘겨주려면 가능한한 위에 붙어서 파이프를 뚫어야만함.
  - 그러므로 dfs돌릴때 위부터 dfs로 뚫고, 만약에 도달하면 바로 끝내야함. 다른거 볼필요X

2. 그리고 만약에 도달하면 걍 체크하고 거기는 안 봐도 됨.

3. 어떤 지점에서 시작해서 도달할 수 있음에도 불구하고 그걸 안하는 경우가 최대가 될 수 있는 경우는 없는듯. (증명?)
  - 그러니까 일단 도달하기만 하면 그거는 무조건 최대인 경우에 포함되는 파이프라 이건데... 증명은 나중에 해보기.
  - 일단 한번 파이프라인이 뚫어지기만 하면, 그거는 무조건 정답이되는 경우에 포함된다 이말임.
  - 귀류로 증명 가능할듯..?

ㅅㅂ 나 천잰가? 한방컷 굿..
"""
# 풀이
import sys

R,C = map(int,sys.stdin.readline().strip().split())

g = [list(sys.stdin.readline().strip()) for _ in range(R)]

di = [-1,0,1]
dj = [1,1,1]

# print(g)
visited = [[0]*C for _ in range(R)]

ans = 0

def dfs(i,j):
    global BRK
    for k in range(3):
        if BRK:
            return
        i_next, j_next = i+di[k] , j+dj[k]
        if 0<=i_next<R and 0<=j_next<C and not visited[i_next][j_next]:
            if j_next == C-1:
                visited[i_next][j_next] = 1
                global ans
                ans += 1
                BRK = True
                return 
            if g[i_next][j_next] == '.':
                visited[i_next][j_next] = 1
                dfs(i_next,j_next)
    

for row in range(R):
    BRK = False
    dfs(row,0)

print(ans)