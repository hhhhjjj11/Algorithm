# 정리
"""
이거는 누적합 문제가 아닌것같은데???
누적합 풀이는 어떻게 하는걵 ㅣ모르겟다
"""
# 풀이
import sys

N = int(input())
li = list(map(int, sys.stdin.readline().strip().split()))

result = 0
for i in range(N):
    cnt = 0
    min = 10**10
    max = -(10**10)
    v = li[i]
    # 왼쪽 건물들에 대하여. 왼쪽에 있는 건물들은 가까이있는 건물들 부터 기울기를 계산해 나갈 때, 기존의 최소기울기보다 더 작아야 보임.
    for j in range(i-1, -1, -1): # i-1 부터 0까지 
        l = (li[i]-li[j])/(i-j)
        # 만약, 기존의 가장 작은 기울기보다 더 작으면.. 최소기울기를 그 값으로 바꾸고. cnt +=1
        if min > l:
            min = l
            cnt += 1

    # 오른쪽 건물들에 대하여. 오른쪽에 있는 건물들의 경우에는 더 커야 보임.
    for k in range(i+1, N):
        l = (li[k]-li[i])/(k-i)

        if max < l:
            max = l
            cnt += 1

    if cnt > result:
        result = cnt

print(result)