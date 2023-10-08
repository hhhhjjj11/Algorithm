# 정리
"""
이중 반복.
근데 3중 이상 따질 필요 X, cnt를 이용.
흐음... 왜 cnt를 사용 하면 알아서 반영이 되는거지. 뭔가 더 따져줘야할것같은데.
앞의 dp에 저장된 값 -> 이미 가장긴 li까지의 수열의 길이가 각각 반영된거임.
그리고 모든 값들은 항상 현재 항을 마지막으로 하는 수열로 생각할 수 잇음.
(앞의 dp값들이 의미하는 수열에다가 지금 항을 붙이기만 하면 되니까.)

- 위와 같이 하면 모든 경우를 따지진 않음. 하지만 최대길이를 구하기는 최적화.
"""

# 풀이l
li1 = list(input())
li2 = list(input())
n1, n2 = len(li1), len(li2)

dp = [0]*n2

for i in range(n1):
    cnt = 0 # 이전까지의 최대길이
    for j in range(n2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif li1[i] == li2[j]:
            dp[j] = cnt + 1

print(max(dp))
