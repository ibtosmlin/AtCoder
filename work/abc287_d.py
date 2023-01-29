# https://atcoder.jp/contests/abc287/tasks/abc287_d
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()
s = list(input())
t = list(input())
T = len(t)

F = [False] * (T+1)
F[0] = True
for i in range(T):
    if s[i] == '?' or t[i] == '?' or s[i] == t[i]:
        F[i+1] = True
        continue
    break

R = [False] * (T+1)
R[0] = True
for i in range(T):
    if s[-i-1] == '?' or t[-i-1] == '?' or s[-i-1] == t[-i-1]:
        R[i+1] = True
        continue
    break
R = R[::-1]

for f, r in zip(F, R):
    print('Yes' if f and r else 'No')