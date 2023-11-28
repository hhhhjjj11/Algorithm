# 정리
"""
완탐으로는 절대 불가. 입력에 따라 3**50 가까이 나올 수 있음. 

핵심: 하나만 건지면 됨. -> aba ca = aab ca = baa ca 같은 경우로 쳐도 무관.
  - 다시말해, aba ca를 가지고 탐색을 한 적이 있다면 aab ca인 경우는 탐색을 하지 않아도 된다.
  - abaca 다음 부분을 채울 수 있다면 항상 aabca의 다음 부분 또한 똑같이 채울 수 있기 때문이다.
  - 똑같이 채울 수 있는 이유는 간단함. 나머지 실행해야할 부분들에 대해 똑같은 조건, 상태를 가지고 있기 때문이다.

  - 같은 조건과 상태 => abaca이후의 탐색과정과 aabca이후의 탐색과정은 완전히 중복된다.
    - 만약에, 가능한 모든 순열을 구해야한다면, 탐색을 해야겠지만 (전체로 봤을땐 다른 순열이므로) 이문제의 경우 가능한 한가지 경우만
구하면 되기때문에, abaca에서 그 다음부분을 완성을 시킬 수 있다 <=> aabca의 그 다음 부분을 완성시킬 수 있다.
따라서 abaca와 aabca를 각각 탐색 할 필요가 없음.

이유: 나머지 실행해야할 부분들에 대해 똑같은 조건, 상태를 가지고 있기 때문.
  - 남은 배열 해야하는 문자들의 종류와 갯수가 같고, 올 수 있는 문자들도 모두 같음.

하지만, 전날 전전날에 뭐가 왔냐는 여전히 중요함. (어떤 조건이 중요하다 = 해당 조건에 따라 이 후의 탐색결과가 달라진다.)

따라서, 같은 것으로 간주해도 무관한 경우 = 갯수와, 전날, 전전날.이 모두 같은 경우들.
"""
# 풀이
import sys

S = sys.stdin.readline().strip()
length = len(S)
Acnt, Bcnt, Ccnt = [S.count(char) for char in ['A','B','C']]

dp = [[[[[0]*3 for _ in range(3)]for _ in range(51)]for _ in range(51)] for _ in range(51)]  # dp[i][j][c][lastlast][last]

A, B, C = 0,1,2

def dfs(a,b,c,last):   # a갯수 b갯수 c갯수, [그제, 어제]
    
    if dp[a][b][c][last[0]][last[1]]:
        return 
    
    if a+b+c == length:
        print(''.join(answer))
        exit(0)

    dp[a][b][c][last[0]][last[1]] = 1
    
    if a<Acnt:
        answer[a+b+c] = 'A'
        dfs(a+1,b,c,[last[1], A])

    if b<Bcnt:
        # 다음에 B가 오려면 어제 B가 오면 안됨
        if last[1] != B:
            answer[a+b+c] = 'B'
            dfs(a,b+1,c, [last[1], B])
    
    if c<Ccnt:
        # 다음에 C가 오려면 어제랑 그제 중에 C가 있으면 안됨.
        if last[1] != C and last[0] != C:
            answer[a+b+c] = 'C'
            dfs(a,b,c+1, [last[1], C])

answer= ['']*(length+1)
dfs(0,0,0,[0,0])
print(-1)