# 정리
"""

"""
# 풀이
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split(""))

graph = [list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]
