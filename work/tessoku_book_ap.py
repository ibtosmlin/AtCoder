# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ap
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
class Imos:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        # 拡張grid生成
        self.grid = [[0] * (w+1) for _ in range(h+1)]

    def import_grid(self, grid):
        for i in range(self.h):
            for j in range(self.w):
                self.grid[i+1][j+1] = grid[i][j]

    def grid_add(self, i, j, ad):
        # i, j is 0 index on self.grid
        self.grid[i][j] += ad

    def accumlate(self):
        # 累積和
        for i in range(self.h+1):
            for j in range(1, self.w+1):
                self.grid[i][j] += self.grid[i][j-1]
        for j in range(self.w+1):
            for i in range(1, self.h+1):
                self.grid[i][j] += self.grid[i-1][j]

    def count(self, x, y, u, v):
        if not 0<= x <= u < self.h+1: return 0
        if not 0<= y <= v < self.w+1: return 0
        gd = self.grid
        return gd[u][v] - gd[u][y] - gd[x][v] + gd[x][y]

###############################################

n, k = map(int, input().split())
im = Imos(110, 110)
for _ in range(n):
    a, b = map(int, input().split())
    im.grid_add(a, b, 1)

im.accumlate()

ret = 0
for i in range(im.h):
    for j in range(im.w):
        u = im.count(i, j, i+k+1, i+k+1)
        ret = max(u, ret)
print(im.grid)
print(ret)