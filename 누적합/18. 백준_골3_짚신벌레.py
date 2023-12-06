# 정리
"""
암기 : dp[i] = i번째 날에 새로태어난 벌레


N 최대 백만, a~b 까지 반복문도 백만 가능해서 이중반복문 돌리면 최악의 경우 10**12 -> 시간초과

흠.. 
일단 덱이랑 리스트도 그렇게 메모리 큰차이도 없는데 왜 풀이2는 메모리초과가 나는건지 모르겠다...
팝하고 어펜드하는게 좀 그런건가 보다..

풀이1로 해도 메모리가 117mb 간당간당하네 (128제한) 
"""
import sys
a,b,d,N = map(int,sys.stdin.readline().strip().split())

dp = [0]*(N+1) # dp[i] = i번째날에 새로 태어난 마리 수
dp[0] = 1

prefix_sum = 0

for i in range(1,N+1):
    prefix_sum += (dp[i-a] - dp[i-b]) % 1000  # i-a와 i-b가 음수이어도 상관이 없음. 어차피 0
    dp[i] = prefix_sum 

print(sum(dp[max(0,N-d+1):N+1])%1000)  # N이 작으면 N-d+1 이 음수가 나올 가능성이 있고 결과가 이상하게 나올 수 있다.


# # 풀이
# import sys
# from collections import deque

# a,b,d,N = map(int,sys.stdin.readline().strip().split())

# record = deque([0]*d)
# record[0] = 1
# toSum = 0

# for _ in range(N):

#     record.appendleft(0)
    
#     # 생식
#     toSum += record[a]
#     toSum -= record[b]
#     record[0] = toSum
#     # 죽임
#     record.pop()

# print(sum(record)%1000)