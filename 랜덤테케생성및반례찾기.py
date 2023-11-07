from random import randint
import random
# subprocess.call

# 예제 생성
def example():

    n = randint(0,10000)
    print('sdfsdfsdfsdfsf')
    # nums = []
    # parent=[1]
    # temp = []
    # while len(nums)<n-2:
    #     p = random.choice(parent)
    #     ch = randint(2,n)
    #     l = randint(1,100)
    #     if not [p,ch] in temp:
    #         nums.append([p,ch,l])
    #     temp.append([p,ch])
    #     parent.append(p)
    # print('n',n, 'nums',nums)
    return n  

# 맞은 답
import sys
sys.setrecursionlimit(10**5)


def right_sol(n):
    n = list(map(int,str(n)))
    l = len(n)
    dp = [0 for _ in range(l+1)]
    if (n[0] == 0) :
        return 0
    else :
        n = [0] + n
        dp[0]=dp[1]=1
        for i in range(2, l+1):
            if n[i] > 0:
                dp[i] += dp[i-1]
            temp = n[i-1] * 10 + n[i]
            if temp >= 10 and temp <= 26 :
                dp[i] += dp[i-2]
        return dp[l] % 1000000


# 틀린 답

def wrong_sol(N):
    N = str(N)
    l = len(N)
    if N[0] == '0':
        return 0
        exit(0)
    dp= [0]*(l+1) # 0~N
    dp[1] = 1
    if l == 1:
        return 1
        exit(0)
    if 0<int(N[0:2])<=26:
        dp[2] = 2
        if int(N[0:2]) == 10 or int(N[0:2]) == 20:
            dp[2] = 1
    elif int(N[1]) == 0:
        return 0
        exit(0) 
    else:
        dp[2] = 1



    i = 3
    if N[-1] == '0' and int(N[-2::]) > 26:
        return 0
        exit(0)

    if l == 2:
        return dp[2]
        exit(0)

    if N[1] == '0' and N[2] == '0':
        return 0
        exit(0)
    while True:
        if i == l+1:
            break
        if int(N[i-2]) == 0:
            dp[i] = dp[i-1] % 1000000
            if N[i-1] == '0':
                return 0
                exit(0)
            i+=1
            continue
        if int(N[i-1]) == 0:
            dp[i] = dp[i-2] % 1000000
            if int(N[i-2]) >= 3 or int(N[i-2]) == 0:
                
                return 0
                exit(0)
            i+=1
            continue
        if int(N[i-2:i]) <= 26:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000
        else:
            dp[i] = dp[i-1] % 1000000
        i+=1
    return dp[l]%(10**6)




# 반례 출력
def check():
    print('sds')
    n = example()
    right = right_sol(n)
    wrong = wrong_sol(n)

    if right != wrong:
        print(n)

        print("맞은 답:", right)
        print("틀린 답:", wrong)
        return
    else:
        print(n)
        check()

check()