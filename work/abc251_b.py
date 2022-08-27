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

n, w = map(int, input().split())
a = list(map(int, input().split()))

ret = set()

for i in range(n):
    ai = a[i]
    if ai<=w:
        ret.add(ai)
    for j in range(i):
        aj = a[j]
        if ai+aj<=w:
            ret.add(ai+aj)
        for k in range(j):
            ak = a[k]
            if ai+aj+ak<=w:
                ret.add(ai+aj+ak)

print(len(ret))