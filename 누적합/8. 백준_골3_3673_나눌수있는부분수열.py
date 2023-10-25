# 정리
"""
ㄷㄷ 7. 백준_골4_2015_수들의합4 이랑 똑같이 푸니까 걍맞네;; 나 혹시 좀 천재?
"""
# 풀이
import sys
from collections import defaultdict

c = int(input())

results =[]
for tc in range(c):
    d, n = map(int, sys.stdin.readline().strip().split())
    
    li = list(map(int, sys.stdin.readline().strip().split()))

    S = [0]*n
    S[0] = li[0]

    for i in range(1,n):
        S[i] = S[i-1] + li[i]
        
    for i in range(n):
        S[i] = S[i]%d
    
    answer = 0
    dic = defaultdict(list)

    for i in range(n):
        if S[i] == 0:
            answer += 1
            answer += len(dic[0])
        else: 
            answer += len(dic[S[i]])
        
        dic[S[i]].append(i)
    
    results.append(answer)

for result in results:
    print(result)