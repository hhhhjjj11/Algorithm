# 정리
"""
product 사용, list 말고 dic사용 (list쓰면 시간초과, dic쓰면 통가ㅗ)
"""

from itertools import combinations, product

def solution(dice):
    n = len(dice)
    # print('n', n)
    all_combinations  = list(combinations(range(n),n//2))
    # print(all_combinations)
    # print('=============================')
    results_list =[[0]*3 for _ in range(len(all_combinations))]

    # 먼저 주사위 절반을 고르고 각 케이스에대하여
    for combination in all_combinations:
        all_sums1={}
        all_sums2={}

        combination_list = list(combination)
        rest_list = list(range(n))
        for x in combination_list:
            rest_list.remove(x)

        dice_outcomes1 = [dice[i] for i in combination]
        # print('dice_outcome1', dice_outcomes1)

        for roll in product(*dice_outcomes1):
            if sum(roll) in all_sums1:
                all_sums1[sum(roll)] += 1
            else:
                all_sums1[sum(roll)] = 1

        dice_outcomes2 = [dice[i] for i in rest_list]
        # print('dice_outcome2', dice_outcomes2)
        
        for roll in product(*dice_outcomes2):
            if sum(roll) in all_sums2:
                all_sums2[sum(roll)] += 1
            else:
                all_sums2[sum(roll)] = 1

        IDX = all_combinations.index(combination)
        # print(all_sums1)
        # print(all_sums2)
        for s1 in all_sums1:
            for s2 in all_sums2:
                if s1>s2:
                    results_list[IDX][0] += all_sums1[s1]*all_sums2[s2]
                elif s1<s2:
                    results_list[IDX][2] += all_sums1[s1]*all_sums2[s2]
                else:
                    results_list[IDX][1] += all_sums1[s1]*all_sums2[s2]
        # for sum1 in all_sums1:
        #     for sum2 in all_sums2:
        #         if sum1 > sum2:
        #             results_list[all_combinations.index(combination)][0] += 1
        #             pass
        #         elif sum1 < sum2:
        #             results_list[all_combinations.index(combination)][2] += 1
        #         else:
        #             results_list[all_combinations.index(combination)][1] += 1

    print(results_list)
    probability =[]
    for result in results_list:
        # print('result', result)
        P = result[0]/sum(result)
        probability.append(P)
    # print(probability)
    res = all_combinations[probability.index(max(probability))]
    # print(res)
    res=list(res)
    for i in range(len(res)):
        res[i] +=1
    return  res


print(solution(

[[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))