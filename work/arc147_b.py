# https://atcoder.jp/contests/arc147/tasks/arc147_b
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
p = list(map(int1, input().split()))


ret = []

def isok(i):
    return i%2 == p[i]%2

def swapA(i):
    ret.append(("A", i+1))
    p[i], p[i+1] = p[i+1], p[i]

def swapB(i):
    ret.append(("B", i+1))
    p[i], p[i+2] = p[i+2], p[i]



for i in range(n):
    if isok(i): continue
    j = i - 2
    while j >= 0 and isok(j):
        swapB(j)
        j -= 2


for i in range(n):
    if isok(i): continue
    swapA(i)


for i in range(n)[::-1]:
    for j in range(i+1):
        if j+2 < n and p[j] > p[j+2]:
            swapB(j)

print(len(ret))
for ri in ret:
    print(*ri)
