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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
n, m = map(int, input().split())
x = list(map(int, input().split()))
c = [0] * (n+1)
for _ in range(m):
    ci, yi = map(int, input().split())
    c[ci] = yi

dp = [-INF] * (n+1)
dp[0] = 0
#dp[i][j]   i回目でカウンタがjの最大値
for i in range(n):
    ndp = [-INF] * (n+1)
    for j in range(n):
        ndp[j+1] = max(ndp[j+1], dp[j] + x[i] + c[j+1])
        ndp[0] = max(ndp[0], dp[j] + c[0])
    dp, ndp = ndp, dp

print(max(dp))