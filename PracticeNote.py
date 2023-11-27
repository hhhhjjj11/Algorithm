N,M=map(int,input().split())

results =[]

def dfs(n, length):
    if length == M:
        temp2= []
        for x in range(N+1):
             temp2.append(temp[x])
        results.append(temp2)
        return
    for next_num in range(1,N+1):
        if temp[length] <= next_num:
            temp[length+1] = next_num
            dfs(next_num, length+1)
    


for i in range(1,N+1):
    temp = [0]*(N+1)
    temp[1] = i
    dfs(i,1)


# print(results)

for result in results:
    for j in range(1,M+1):
        if j==M:
            print(result[j])
            continue
        print(result[j], end=' ')