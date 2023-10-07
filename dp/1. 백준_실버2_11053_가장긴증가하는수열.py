# 정리
"""
1. 기본 개념 : 다 해보면서 답이 바뀔경우 기록을 바꾼다.
2. 어떤 방향으로 탐색해나갈것인지. 이 문제의 경우 앞에서부터 뒤로 찾아나가면되고.
3. 1더한 값과 기존값을 비교한다는점.
"""
# 풀이
import sys

N = int(input())
li = list(map(int,input().split()))
dp = [1]*N
for i in range(1,N):
    for j in range(i):
        if li[i]>li[j]:
            dp[i]= max(dp[i], dp[j] +1)

print(max(dp))