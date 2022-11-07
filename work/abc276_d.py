# https://atcoder.jp/contests/abc276/tasks/abc276_d
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
n = int(input())
a = list(map(int, input().split()))

two = []
three = []
other = []

for ai in a:
    cnt = 0
    while ai%2 ==0:
        cnt += 1
        ai //= 2
    two.append(cnt)
    cnt = 0
    while ai%3 ==0:
        cnt += 1
        ai //= 3
    three.append(cnt)

    other.append(ai)

if other != [other[0]] * len(other):
    end(-1)

m3 = min(three)
m2 = min(two)

ret = sum(two) - m2*n
ret += sum(three) - m3*n
print(ret)