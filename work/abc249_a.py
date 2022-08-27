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

a, b, c, d, e, f, x = map(int, input().split())

taka = 0
aoki = 0

tn = x
while tn >= a+c:
    taka += b*a
    tn -= a+c

taka += min(tn, a) * b

ta = x
while ta >= d+f:
    aoki += d*e
    ta -= d+f

aoki += min(ta, d) * e

if taka > aoki:
    print('Takahashi')
elif taka < aoki:
    print('Aoki')
else:
    print('Draw')