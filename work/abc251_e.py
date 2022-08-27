import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()

n = int(input())
a = list(map(int, input().split()))

#dp[i][j]  i番目の行動をしたかどうかj=0,j=1かどうか。


dp = [[[INF]*2 for j in range(n)] for k in range(2)]
dp[0][0] = [0, INF]
dp[1][0] = [INF, 0]
for i in range(n):
    ai = a[i]
    for k in range(2):
        dp[k][i][1] = min(dp[k][i][1], dp[k][i-1][0] + ai)
        dp[k][i][1] = min(dp[k][i][1], dp[k][i-1][1] + ai)
        dp[k][i][0] = min(dp[k][i][0], dp[k][i-1][1])

print(min(dp[0][-1][0], dp[1][-1][1]))