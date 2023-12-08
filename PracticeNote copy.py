import bisect

arr = [1, 2, 4, 7, 9, 12]
target = 12

# target을 삽입할 위치를 찾음
index = bisect.bisect_left(arr, target)
print('index',index)
if index < len(arr):
    result = arr[index]
    print(f"{target}보다 작지 않은 가장 작은 값: {result}")
else:
    print(f"{target}보다 작지 않은 값이 배열에 없습니다.")