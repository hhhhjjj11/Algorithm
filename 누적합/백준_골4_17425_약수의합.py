# 정리
"""
에라토스테네스 체 푸는것마냥 푼다.. 즉 작은 수부터 배수처리해간다.

답을 한번에 출력하면 시간초과가 안나고, 
답을 테케마다 출력하면 시간초과가 난다. 이유는 모르겠다.

"""

# 풀이
MAX = 1000000
dp = [1]*(MAX+1) # dp[i] = i의 약수의 합
s = [0]*(MAX+1) # s[i] = g(i)

for i in range(2,MAX+1):
    j = 1
    while i*j < MAX+1:
        dp[i*j] += i
        j+=1

for i in range(1,MAX+1):
    s[i] = dp[i] + s[i-1]

# tc = int(input())
# for _ in range(tc):
#     N = int(input())
#     print(s[N])

n = int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(s[a])

for x in ans:
    print(x)

# print('\n'.join(map(str, ans))+'\n')