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

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
#リストの作成
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append(b)

def bfs(s):
    seen = [False] * n
    que = deque()
    que.append([s])
    seen[s] = True
    while que:
        path = que.popleft()
        nw = path[-1]
        for nx in edges[nw]:
            if nx == s:
                return path
            if seen[nx]:
                continue
            else:
                que.append(path + [nx])
                seen[nx] = True
    return False

ret = [-1] * 1010
for i in range(n):
    nw = bfs(i)
    if nw == False: continue
    if len(nw) < len(ret):
        ret = nw

if ret[0] == -1:
    end(-1)
print(len(ret))
for i in ret:
    print(i+1)
