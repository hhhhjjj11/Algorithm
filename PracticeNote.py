from typing import List

def solution(fees: List[List[int]], t: int) -> List[int]:
    answer = []
    fees.sort()
    a_Max = 0
    a_min = 0
    
    dic = {}
    keys = []
    for time, fee in fees:
        if fee in dic:
            dic[fee].append(time)
        else:
            dic[fee] = [time]
            keys.append(fee)
        
    # print(dic)
    # # print(dic[list(dic.keys())[1]])
    # print(keys)

    for i in range(len(dic)):
        # a_min 찾기
        if max(dic[keys[i]]) - min(dic[keys[i]]) + 1 > a_min:
            a_min = max(dic[keys[i]]) - min(dic[keys[i]]) + 1
        
        # a_Max 찾기
        if i >= 2:
            if min(dic[keys[i]]) - max(dic[keys[i-2]]) - 1 > a_Max:
                a_Max = min(dic[keys[i]]) - max(dic[keys[i-2]]) - 1

        elif i == 1:
            if min(dic[keys[i]]) > a_Max:
                a_Max = min(dic[keys[i]])

    # print('M,m', a_Max, a_min)

    results = []

    for a in range(a_min, a_Max + 1):
        # b 찾기
        X1 , X2 = min(dic[keys[0]]), max(dic[keys[0]])
        K = 1

        while True:
            if (K-1)*a <=X1 and X2 < K*a:
                if keys[0] % K: # 나머지가 0이아니면 즉 자연수가 아니면
                    b = 0 
                    break
                else: # 자연수면
                    b = keys[0] // K 
                    break
            elif X1 < K*a <= X2:
                b = 0
                break
            K += 1

        if not b:
            continue

        # print(b)

        flag = True
        for fee in dic:
            if fee % b:
                flag = False
                break
            K = fee//b
            X3, X4 = min(dic[fee]), max(dic[fee])
            if not((K-1)*a <= X3 and X4 < K*a):
                flag = False
                break
        if flag:
            results.append([a,b])
        
    # print('a,,b', results)
    values = []    

    if not len(results):
        return [-1]
    
    for a,b in results:
        values.append(b * ((t // a) + 1))

    return [min(values), max(values)]

# 시간,요금
print(solution(
[[4, 1000], [6, 1000], [21, 3000], [16, 2000], [26, 3000]], 27))