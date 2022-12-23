# https://atcoder.jp/contests/abc173/tasks/abc173_c
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
h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

def check(i, j):
    cnt = 0
    for u in range(h):
        if i >> u & 1: continue
        for v in range(w):
            if j >> v & 1: continue
            if c[u][v] == '#':
                cnt += 1
    return cnt == k


ret = 0
for i in range(1<<h):
    for j in range(1<<w):
        ret += check(i, j)
print(ret)