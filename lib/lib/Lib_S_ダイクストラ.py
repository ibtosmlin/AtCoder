#name#
# ダイクストラ法
#description#
# ダイクストラ法
# 辺の重みが小さいものから、決めていく

#body#
# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
class dijkstra:
    def __init__(self, n, G):
        self.n = n              # ノード数
        self.G = G      # 有向グラフ
        self.start = None       # 始点
        self.G_used = [None] * n  # 最短経路木の親

    def build(self, start):
        self.dist = [INF] * self.n
        next_q = []
        if type(start) is int:
            start = [start]
        for st in start:
            self.dist[st] = 0
            next_q.append((0, st))
        heapify(next_q)
        while next_q:
            cd, cn = heappop(next_q)
            if self.dist[cn] < cd: continue
            for nn, nd in self.G[cn]:
                # 変則的な距離の場合はここを調整 ##
                nd_ = self.dist[cn] + nd
                ############################
                if self.dist[nn] <= nd_: continue
                self.dist[nn] = nd_
                self.G_used[nn] = cn
                heappush(next_q, (nd_, nn))


    def get_dist(self, goal):
        return self.dist[goal]


    def get_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.G_used[node]
        return path[::-1]

##########################################

n, m, t = map(int, input().split())
G = [[] for _ in range(n)]
G_R = [[] for _ in range(n)]    #行きと帰りを分けた（有向グラフ）場合
#リストの作成
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((b,c))
    G[b].append((a,c))
    G_R[b].append((a,c))        #行きと帰りを分けた（有向グラフ）場合

dij = dijkstra(n, G)  #クラスのインスタンス化
dijR = dijkstra(n, G_R)
dij.build(0)
dijR.build(0)

dij.get_dist(n-1)

#prefix#
# Lib_S_最短経路探索_dijkstra
#end#
