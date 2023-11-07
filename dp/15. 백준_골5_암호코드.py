# 정리
"""
아이디어는 쉬운데 함정 존나 많은 문제;;
개ㅈ같은문제네
"""
# 풀이
N = input()
l = len(N)
if N[0] == '0':
    print(0)
    exit(0)
dp= [0]*(l+1) # 0~N
dp[1] = 1
if l == 1:
    print(1)
    exit(0)
if 0<int(N[0:2])<=26:
    dp[2] = 2
    if int(N[0:2]) == 10 or int(N[0:2]) == 20:
        dp[2] = 1
elif int(N[1]) == 0:
    print(0)
    exit(0) 
else:
    dp[2] = 1

i = 3
if N[-1] == '0' and int(N[-2::]) > 26:
    print(0)
    exit(0)

if l == 2:
    print(dp[2])
    exit(0)

if N[1] == '0' and N[2] == '0':
    print(0)
    exit(0)
while True:
    if i == l+1:
        break
    if int(N[i-2]) == 0:
        dp[i] = dp[i-1] % 1000000
        if N[i-1] == '0':
            print(0)
            exit(0)
        i+=1
        continue
    if int(N[i-1]) == 0:
        dp[i] = dp[i-2] % 1000000
        if int(N[i-2]) >= 3 or int(N[i-2]) == 0:
            
            print(0)
            exit(0)
        i+=1
        continue
    if int(N[i-2:i]) <= 26:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000
    else:
        dp[i] = dp[i-1] % 1000000
    i+=1
print(dp[l]%(10**6))