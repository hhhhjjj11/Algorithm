def solution(friends, gifts):
 
    N = len(friends)
    record =[[0]*N for _ in range(N)]
    results = [0]*N

    # 입력데이터 gifts를 통해서 record를 완성 
    # record[i][j] = i번 친구가 j번 친구에게 준 선물 갯수
    for gift in gifts:
        A,B = gift.split()
        friends_idx_of_A = friends.index(A)
        friends_idx_of_B = friends.index(B)
        # print(friends_idx_of_A,friends_idx_of_B)
        record[friends_idx_of_A][friends_idx_of_B]+=1
        # print(A,B)

    # print(record)
    temp = [0]*N
    # 이제, 선물 예측.
    for i in range(N):
        for j in range(i+1,N):
            if i==j:
                continue
            # print(i,j,'비교')
            # print(friends[i],friends[j],'비교')
            # 두 사람 사이에 주고받은 선물이 차이가 있으면
            ItoJ, JtoI = record[i][j], record[j][i]
            if ItoJ > JtoI: # I가 준게 더 많으면
                # print('i가준게 더 많음')
                # print(friends[i], '+1')
                results[i]+=1
                # print('1=====', results)
            elif ItoJ < JtoI:
                # print('j가준게 더 많음')
                # print(friends[j],' +1')
                results[j]+=1
                # print('2=====', results)

            else: # 주고 받은 갯수가 같으면
                # 선물지수를 따져야함.
                # 선물지수 = 준 선물 갯수 - 받은 선물 갯수
                present_value_of_i, present_value_of_j = 0,0
                # 준거 더하기
                present_value_of_i += sum(record[i])
                present_value_of_j += sum(record[j])
                # 받은거 빼기
                for p in range(N):
                    present_value_of_i -= record[p][i]
                    present_value_of_j -= record[p][j]

                if present_value_of_i > present_value_of_j:
                    results[i] += 1
                    # print(friends[i], '+1')
                    # print('3=====', results)
                elif present_value_of_i < present_value_of_j:
                    results[j] += 1
                    # print(friends[j],' +1')
                    # print('4=====', results)
                temp[i]= present_value_of_i
                temp[j] = present_value_of_j
                # 같으면 주고받지 않음.
    # print(temp)
    # print(results)
    return max(results)



print(solution(
["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))