# 정리
"""
걍 빡구현;; 빡시노
"""
# 풀이
import sys

R,C,M = map(int, sys.stdin.readline().strip().split())

SHARK = []

for _ in range(M):
    i,j,v,d,z = map(int,sys.stdin.readline().strip().split())
    # 위 아래로 움직일 경우에는 2R-2 로 나눈 나머지
    if d == 1 or d==2:
        v %= 2*R - 2
    # 좌우로 움직일 경우에는 2C-2 로 나눈다.
    elif d== 3 or d== 4:
        v %= 2*C - 2
    
    SHARK.append([i,j,v,d,z])


if not M:
    print(0)
    exit(0)

# 위치 위치 속력 이동방향 크기

# 위 아래 오 왼
di = ['empty', -1,1,0,0]
dj = ['empty', 0,0,1,-1]

eaten = [0]*M

def findCloseShark(j):
    # print('가장가까운 상어찾기, 낚시꾼위치', j)
    minRow = R+1
    resNum = -1
    for shNum in range(M):
        if j == SHARK[shNum][1] and minRow > SHARK[shNum][0] and not eaten[shNum]:
            minRow = SHARK[shNum][0]
            resNum = shNum
    return resNum


def sharkMove():
    
    WATER = [[[] for _ in range(C+1)] for _ in range(R+1)]

    for shk in range(M):
        # 이미 먹힌 상어는 계산노노
        if eaten[shk]:
            # print('먹힌상어', shk)
            continue
        
        # print('==========')
        # print(shk, '번 상어 이동 시작')
        # print(SHARK[shk])
        # print('==========')/
        # 속도 만큼 움직인다
        i_now, j_now, v, d, size = SHARK[shk]
        i_next, j_next = i_now + di[d]*v , j_now + dj[d]*v

        # 만약에 칸 밖으로 벗어나면 방향 반대됨
        if not (0<i_next<=R and 0<j_next<=C):
            toMove = v
            # print(SHARK[shk])
            while toMove:
                # print('now' ,i_now,j_now)
                # print('toMove',toMove)
                # print('d', d)
                if 0<i_now + di[d]<=R and 0<j_now + dj[d]<=C:
                    i_now += di[d]
                    j_now += dj[d]
                    # print('sdfsdf')
                else:
                    if d == 2: 
                        d=1
                    elif d==1:
                        d=2
                    elif d==3:
                        d=4
                    elif d==4:
                        d=3
                    continue
                toMove-=1
            i_next,j_next = i_now,j_now

        # print('결과', i_next,j_next,d)
        WATER[i_next][j_next].append([size,shk])
        
        SHARK[shk][0], SHARK[shk][1], SHARK[shk][3] = i_next, j_next, d
    
    # print('상어들의 이동결과..............')
    # print(WATER)

    # 이동한다음에 겹치는 애들 있으면 제일 큰상어가 다 먹음
    for i in range(1,R+1):
        for j in range(1,C+1):
            if len(WATER[i][j])>1:
                # 가장 사이즈가 큰 상어를 찾고
                M_size , M_shk = max(WATER[i][j])
                # print('===', WATER[i][j])
                for size, num in WATER[i][j]:
                    if M_size > size:
                        eaten[num] = 1

total = 0

for j in range(1, C+1):
    # print('=-=========================================================================')
    # 1. 이동, 낚시꾼의 위치 = j + 1
    fisherMan = j 
    # 2. 가장 위에 있는 상어를 낚기.
    #   - 가장 위에 있는 상어를 찾아야함.
    sharkNUM = findCloseShark(fisherMan)
    # print('위치',j,'에서 가장 가까운 상어',sharkNUM, '/' ,SHARK[sharkNUM])
    if sharkNUM != -1 and not eaten[sharkNUM]:
        total += SHARK[sharkNUM][4]
        # print('먹힘')
        eaten[sharkNUM] = 1

    # 이제, 상어 이동...
    sharkMove()

    
print(total)