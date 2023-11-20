# 정리
"""
왠지 2차원 dp테이블을 활용해아할 것 같음.
"""
# 풀이
import sys

N = int(input())

if N < 10:
    print(0)
    exit(0)


dp = []
# 예 11
# 12345676789