# 정리
"""
이거는 걍 통째로 외워야 할듯

풀이 순서
1. 누적합 배열 적고
2. 앞에서부터 (뭐 또는 뒤에서부터)
 각 합 체크, 목표값 설정, 목표값을 갖는 인덱스가 있는지 체크. 이때 dic활용. 
 이 때 dic = {sum: [idx1, idx2]} (키가 누적합이고 값이 해당 값을 누적합으로 갖는 인덱스들..)
"""
# 풀이
import sys

N, K = map(int,sys.stdin.readline().strip().split())

li = list(map(int,sys.stdin.readline().strip().split()))

S = [0]*N
S[0] = li[0]
for i in range(1, N):
    S[i] = S[i-1] + li[i]
    
answer = 0
dic = {} 
for i in range(N):
    
    if S[i] == K:
        answer += 1
    
    target = S[i] - K

    if target in dic:
        answer += len(dic[target])
    
    
    if S[i] in dic:
        dic[S[i]].append(i)
    else:
        dic[S[i]] = [i]

print(answer)