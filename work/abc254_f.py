# https://atcoder.jp/contests/abc254/tasks/abc254_f
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
class SegmentTree:  # 初期化処理
    """Segment Tree
    一点更新・区間集約
    Parameters
    ----------
    init : list
        初期リスト
    f : SegmentTreeにのせるモノイド
        作用素
    ie : fに対する単位元
    Notes
    -----
    1-indexed
    https://atcoder.jp/contests/practice2/tasks/practice2_j
    モノイドとは、集合と二項演算の組で、結合法則と単位元の存在するもの
    ex. +, max, min
    [ 1] a0 ・ a1  ・ a2 ・ a3 ・ a4 ・ a5 ・ a6 ・ a7  ->[0]
    [ 2] a0 ・ a1  ・ a2 ・ a3       [ 3] a4 ・ a5 ・ a6・ a7
    [ 4] a0 ・ a1    [ 5] a2 ・ a3   [ 6] a4 ・ a5   [ 7] a6 ・ a7
    [ 8] a0 [ 9] a1  [10] a2 [11] a3 [12] a4 [13] a5 [14] a6 [15] a7
                          [0001]
              [0010]                  [0011]
        [0100]      [0101]      [0110]      [0111]
     [1000][1001][1010][1011][1100][1101][1110][1111]
    size = 8  元の配列数の２べき乗値
    親のインデックス         i//2 or i>>=1 bitで一個右シフト
    左側の子のインデックス    2*i
    右側の子のインデックス    2*i+1
    aiの値が代入されているインデックス    i+size
    """
    def __init__(self, init, f, ie):
        self._f = f
        self._ie = ie
        if type(init) == int:
            init = [ie] * init
        self._n = len(init)
        self._log = (self._n - 1).bit_length()  # seg木の深さ
        self._size = 1 << self._log     # seg木のサイズ
        # seg木の初期化
        self._dat = [ie] * self._size + init + [ie] * (self._size - len(init))
        for i in range(self._size-1, 0, -1):
            self._update(i)


    def _update(self, i):
        # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
        self._dat[i] = self._f(self._dat[i*2], self._dat[i*2+1])


    def __getitem__(self, i):
        """index = i の値を求める
        """
        return self._dat[i + self._size]


    def __str__(self):
        """元のリストの値を表示
        """
        return ' '.join(map(str, (self[i] for i in range(self._n))))


    def update(self, i, x):
        """one point update
        a[i] を xに更新
        """
        #
        i += self._size
        self._dat[i] = x
        while i > 0:    # 層をのぼりながら値を更新 indexが0になれば終了
            i >>= 1     # 1つ上の層のインデックス(完全二分木における親)
            # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
            self._update(i)


    def add(self, i, x):
        """one point update
        a[i] に xを加算
        """
        #
        i += self._size
        self._dat[i] += x
        while i > 0:    # 層をのぼりながら値を更新 indexが0になれば終了
            i >>= 1     # 1つ上の層のインデックス(完全二分木における親)
            # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
            self._update(i)


    def query(self, l, r):
        """半開区間[l, r)にf(a[l], a[l+1])演算
        """
        # モノイドでは可換律は保証されていないので演算の方向に注意
        l += self._size  # 1番下の層におけるインデックス
        r += self._size  # 1番下の層におけるインデックス
        # 左側の答えと右側の答えを初期化
        lret, rret = self._ie, self._ie
        while l < r:    # lとrが重なるまで上記の判定を用いて演算を実行
            # 左が子同士の右側(lが奇数)(lの末桁=1)ならば、dat[l]を演算
            if l & 1:
                lret = self._f(lret, self._dat[l])
                l += 1
            # 右が子同士の右側(rが奇数)(rの末桁=1)ならば、dat[r-1]を演算
            if r & 1:
                r -= 1
                rret = self._f(self._dat[r], rret)
            l >>= 1
            r >>= 1
        return self._f(lret, rret)


    def max_right(self, l, isOk):
        """
        ex:
        maxの場合 a[l]  a[r-1] が isOKとなる最大の値
        (1): 関数 bool isOk(x) を定義し、segtreeの上で二分探索をする。
        (2): 木の値を引数にとりboolを返す関数オブジェクトを渡して使用します。
        r = l もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
        r = n もしくは f(op(a[l], a[l + 1], ..., a[r])) = false
        fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最大のr
        """
        if l >= self._n: return self._n
        l += self._size
        sm = self._ie
        while True:
            while l % 2 == 0: l >>= 1
            if not isOk(self._f(sm, self._dat[l])):
                while l < self._size:
                    l <<= 1
                    if isOk(self._f(sm, self._dat[l])):
                        sm = self._f(sm, self._dat[l])
                        l += 1
                return l - self._size
            sm = self._f(sm, self._dat[l])
            l += 1
            if l & -l == l: break
        return self._n


    def min_left(self, r, isOk):
        """
        l = r もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
        l = 0 もしくは f(op(a[l-1], a[l], ..., a[r-1])) = false
        fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最小のl
        """
        if r <= 0: return 0
        r += self._size
        sm = self._ie
        while True:
            while r > 1 and r % 2 == 1: r >>= 1
            if not isOk(self._f(self._dat[r], sm)):
                while r < self._size:
                    r = r << 1 | 1
                    if isOk(self._f(self._dat[r], sm)):
                        sm = self._f(self._dat[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._f(self._dat[r], sm)
            if r & -r == r: break
        return 0


####################################
class RMaxQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, max, -float('inf'))

class RMinimumQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, min, float('inf'))

class RSumQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, lambda x, y: x + y, 0)

class RProdQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, lambda x, y: x * y, 1)

class RXorQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, lambda x, y: x ^ y, 0)

# GCD query
from math import gcd
ie = 0
def op(x, y):
    if x == ie: return y
    if y == ie: return x
    return gcd(x, y)


####################################


n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

da = [a[i]-a[i-1] for i in range(1, n)]
db = [b[i]-b[i-1] for i in range(1, n)]

sgta = SegmentTree(da, op, ie)
sgtb = SegmentTree(db, op, ie)

for _ in range(q):
    la, ra, lb, rb = map(int1, input().split())

    A = sgta.query(la, ra)
    B = sgtb.query(lb, rb)

    print(gcd(gcd(A, B), a[la] + b[lb]))

