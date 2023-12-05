# 정리
"""
어렵지 않음 걍.. 생각한대로 구현하면 되는게 맞아

"""
# 풀이
import sys
from collections import Counter

T = int(input())
n = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().strip().split()))

# print(A, B)

c = Counter()
for s in range(n):
    for e in range(s,n):
        c[sum(A[s:e+1])] += 1

result = 0

for s in range(m):
    for e in range(s,m):
        temp = sum(B[s:e+1])
        result += c[T - temp]

print(result)
    