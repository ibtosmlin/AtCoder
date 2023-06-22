# https://atcoder.jp/contests/abc306/tasks/abc306_d
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
n = int(input())
dp = [0] * 2
# 元気、壊す、死ぬ

for _ in range(n):
    x, y = map(int, input().split())
    ndp = [-INF, -INF]
    if x == 0:
        ndp[0] = max(dp[0] + y, dp[0], dp[1] + y)
        ndp[1] = dp[1]
    else:
        ndp[0] = dp[0]
        ndp[1] = max(dp[0] + y, dp[1])
    dp = ndp

print(max(dp))
