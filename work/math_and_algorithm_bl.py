# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bl
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
INF = 10**9
def calc(N, E, s):
    G = [[] for i in range(N)]
    for a, b, d in E:
        # x_a - x_b <= d
        G[b].append((a, d))

    INF2 = INF**2
    dist = [INF2] * N
    dist[s] = 0
    update = 1
    for _ in range(N):
        update = 0
        for v in range(N):
            for w, d in G[v]:
                if dist[v] + d < dist[w]:
                    dist[w] = dist[v] + d
                    update = 1
        if not update:
            break
    else:
        return None
    for i in range(N):
        dist[i] = min(dist[i], INF)
    # dist[i]: the maximum value of (x_i - x_s)
    return dist

n, m = map(int, input().split())
E = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    E.append((a, b, c))
    E.append((b, a, c))
ret = calc(n, E, 0)[-1]
if ret == INF:
    print(-1)
else:
    print(ret)

# => "[0, 3, 8]"