# https://atcoder.jp/contests/past202303-open/tasks/past202303_g
from itertools import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys; sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a'): return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a'): return ord(a)-ord(base)
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): exit(print(r))
h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
ret = set()
for i in range(h):
    for j in range(w):
        a = A[i][j]
        if i+1 < h:
            b = A[i+1][j]
            if a > b:
                ret.add((b, a))
            else:
                ret.add((a, b))
        if j+1 < w:
            b = A[i][j+1]
            if a > b:
                ret.add((b, a))
            else:
                ret.add((a, b))
ret = sorted(ret)
for a, b in ret:
    print(a, b)