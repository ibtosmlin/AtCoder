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
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
def distPtoP(pt1, pt2): return dist2(pt1, pt2) ** 0.5
def distCtoC(c1, c2):
    pt1, r1 = c1; pt2, r2 = c2; R, r, d = max(r1, r2), min(r1, r2), dist(pt1, pt2)
    return d-R-r if d > R+r else R-r-d if d < R-r else 0
n = int(input())
dp = [-INF] * 5
dp[0] = 0
pt = 0
for i in range(n):
    ndp = [0] * 5
    t, x, ai = map(int, input().split())
    for ps in range(5):
        ndp[ps] = dp[ps]
        for pp in range(5):
            if pp - (t - pt) <= ps <= pp + (t - pt) and ps != x:
                ndp[ps] = max(ndp[ps], dp[pp])
            if pp - (t - pt) <= ps <= pp + (t - pt) and ps == x:
                ndp[ps] = max(ndp[ps], dp[pp] + ai)
    pt = t
    dp = ndp
print(max(dp))