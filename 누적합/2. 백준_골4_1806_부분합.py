# 정리
"""

이거는 생각해보면 누적합 dp메모 써도 2중 반복문을 돌려야하기때문에 10^10번 연산필요임. 
따라서 누적합 dp 도 시간 초과임.

커서이용!!!!!!!!!!

1. min 은 100000이 아니라 100001로.
2. 문제조건 제대로 읽기 다더해도 S못넘는 경우 분기 해줘야 함.

"""

# 풀이
import sys

N, S = map(int, sys.stdin.readline().strip().split())

li = list(map(int, sys.stdin.readline().strip().split()))

i, j = 0,0
sum = li[0]
min =100001

while True:

    if sum >= S:
        if min > j-i+1:
            min = j-i+1
        sum -=li[i]
        i+=1
        
    
    else:
        j+=1
        if j==N:
            break
        sum+=li[j]


print(0) if min == 100001 else print(min)