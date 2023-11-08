# 정리
"""
일단 에라토스테네스의 체를 쓰긴하는데 조금 변형시켜야함
소수찾듯이 1부터 쫙 하면 M크기의배열이필요한데 이렇게 하면 메모리초과가 난다는 점.

그러면 원하는 배열의 크기만큼 만들기 위해 M-m+1 크기의 배열을 만들고
그다음 m ~ M를 반영한 범위에서만 생각한다
"""

# 풀이

m,M = map(int,input().split())

li = [0]*(M-m+1) # 0:m ~ M-m:M
if M == 1:
    print(1)
    exit(0)

for i in range(2, int(M**(0.5)) + 1):
    square = i**2
    # 이제 범위를 추려주기 위해 m 과 M 사이의 square의 배수들만을 찾는다.
    if m/square == m//square:
        for X in range((m//square)*square, M+1,square):
            print('dd',X)
            li[X-m] = 1
    else: 
        for X in range(((m//square)+1)*square, M+1,square):
            print('dd',X)
            li[X-m] = 1
    # ((m//square)+1)*square : m 보다 작지 않으면서 가장 작은 square 의 배수.
    # 수정 -> ((m//square)+1)*square : m 보다 크면서 가장 작은 square 의 배수.
    # 따라서 위와 같이 하면 m자체가 제곱수의 배수인 경우를 체크할 수업승ㅁ
result = 0
for i in range(M-m+1):
    if not li[i]:
        result+=1

print(result)