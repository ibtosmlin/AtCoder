#####################################
# 最長増加部分列 dp[k]
# 今まで見た来たものの中で、単調増加(非減少)な部分列であって、
# 長さ k であるようなもののうち、その最後の要素の最小値
# 新しいアイテムuだったとき
# dp[k] < u となる一番右の列(k)を特定しその次のdp[k+1]を小さければ更新する
# rem: kに対して単調増加
from bisect import bisect, bisect_left

class LIS:
    """
    fg: 0:単調非減少, 1:単調増加
    """
    def __init__(self, x:list, fg=1):
        n = len(x)
        res = [0] * n
        dp = []
        for i, xi in enumerate(x):
            if fg == 0: # 非減少
                pos = bisect(dp, xi)
            elif fg == 1: # 単調増加
                pos = bisect_left(dp, xi)
            res[i] = pos + 1
            if len(dp) <= pos:
                dp.append(xi)
            else:
                dp[pos] = xi
        self.length = len(dp)
        restore = []
        nw = self.length
        for i in range(n)[::-1]:
            if nw == res[i]:
                restore.append(x[i])
                nw -= 1
        restore.reverse()
        self.restore = restore
        self.lis = dp
        self.res = res



####################################

n = int(input())
lr = []
for _ in range(n):
    l, r = map(int, input().split())
    lr.append([l, -r])
lr.sort()

a = []

for l, r in lr:
    a.append(r + 10**9)

print(LIS(a,0).length)

