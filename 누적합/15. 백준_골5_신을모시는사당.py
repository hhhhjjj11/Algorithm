# 정리
"""
아이디어 알겠는데 
직관과 지구반대편에 위치. 이게 왜 골4??

BBAAABAAAA
처음부터 현재까지 A카운트 - 처음부터 지금까지 중 가장 컸던 B카운트  => B가 가장 많을 가능성
처음부터 현재까지 B카운트 - 처음부터 지금까지 중 가장 컸던 B카운트  => A가 가장 많을 가능성.

다른 방법 없나????? 뭔가 너무 꼬아서 생각하고있는것 같은데 
애초에 누적합으로부터 구간합을 구하기 위해서는 뺄셈이 필연적이기 때문에
누적합 개념을 이용해서 풀때는 위와같은 뺄셈식을 통해 최대를 구해야하므로 반대경우의 최대를 빼는 식으로 접근하는게
맞는건가..? 
"""
# 풀이
import sys

N = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))

S = [0]*N               # S[i] = i번째까지 합

v=0

S[0] =li[0]

for i in range(1,N):
    if li[i] == 2:
        li[i] = -1

    S[i] = S[i-1] + li[i]    # S[i] = i 번째 까지의 계산 

L,R = 0,0
M = 0
while True:
    if L == R:
        temp = S[R]       # L에서 R까지 
    else:
        temp = S[R] - S[L-1]  # R에서 ㄴ까지의 합
    
    if temp >= M:
        M = temp
        if R == N-1:
            R += 1
        else:
            L += 1
        
    else:
        L += 1
    
    if L==N:
        break
        
print(M)