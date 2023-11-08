m,M = map(int,input().split())

li = [0]*(M+1) 
if M == 1:
    print(1)
    exit(0)

for i in range(2, M):
    if not li[i]:
        k = 1
        while (i**2)*k <= M:
            li[(i**2)*k] = 1
            k += 1

result = 0
for i in range(m,M+1):
    if not li[i]:
        result+=1

print(result)