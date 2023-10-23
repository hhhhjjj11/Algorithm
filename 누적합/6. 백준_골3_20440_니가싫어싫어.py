# 정리
"""
리스트로하면 모든 구간에 다 만들어야하니까 시작이랑 끝만 체크한다.. dic이용해서..
굿굿
"""
# 풀이
import sys

N = int(input())
dic = {}

for _ in range(N):
    IN, OUT = map(int,sys.stdin.readline().strip().split())
    dic[IN] = dic.get(IN,0) + 1
    dic[OUT] = dic.get(OUT,0) - 1

total = 0
M = 0
s,e=0,0

times = sorted(dic.keys())

for time in times:
    total += dic[time]

    if total > M:
        M = total
        s = time
        check  = True
    elif total < M and check:
        e = time
        check = False

print(M)
print(s,e)
