from collections import defaultdict
from heapq import *


def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)   #定义一个空字典、此字典若没找到key，则返回空列表[]
    for l, r, c in edges: #l:源点、r:终点 c:距离
        g[l].append((c, r)) #建立一个字典，元素是源点为key、（距离，终点）为value

    q, seen = [(0, from_node, ())], set() #初始化优先队列、初始化已找到的最短路径集合——————元组（源点到点A的距离，某个点A，源点到点A的路径）
    while q: #优先队列为空时，循环结束
        (cost, v1, path) = heappop(q) #从优先队列中找出与源点距离最小的点
        if v1 not in seen:  #若点v1以确定最短路径则无需计算
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path #返回到终点的信息
            for c, v2 in g.get(v1, ()): #更新优先队列，加入与当前点相连的所有点的信息
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return float("inf"), []


def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. Get the length firstly;
        ## 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 Record the destination node firstly;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()  ## 3. Reverse the list finally, to make it be normal sequence.
    return len_shortest_path, ret_path


### ==================== Given a list of nodes in the topology shown in Fig. 1.
list_nodes_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
### ==================== Given constants matrix of topology.
M = 99999  # This represents a large distance. It means that there is no link.
### M_topo is the 2-dimensional adjacent matrix used to represent a topology.
M_topo = [
    [M, 1, 1, M, 1, M, 1, 1, 1, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, 1, M, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [M, M, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, 1, M, M, M, M, M, 1, 1, 1, M, M, M, M, M, M, M, M, M],
    [M, 1, M, M, M, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, M, M, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, M, M, M, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, M, M, M, M, 1, M, 1, M, M, 1, M, M, M, M, M, M, M, M],
    [M, M, M, M, 1, M, M, M, 1, M, M, 1, M, M, M, M, M, M, M, M, M],
    [M, M, M, M, 1, M, M, M, M, M, M, 1, M, 1, M, M, M, M, M, M, M],
    [M, M, M, M, 1, M, M, M, M, 1, 1, M, M, 1, 1, M, M, M, M, M, M],
    [M, M, M, M, M, M, M, M, 1, M, M, M, M, M, 1, M, M, M, M, M, M],
    [M, M, M, M, M, M, M, M, M, M, 1, 1, M, M, 1, M, M, 1, 1, M, M],
    [M, M, M, M, M, M, M, M, M, M, M, 1, 1, 1, M, 1, 1, M, M, M, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, 1, M, 1, 1, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, 1, M, M, M, M, 1],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, M, M, M, 1, M, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, 1, M, 1, M, 1, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, M, 1, M, 1],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, M, 1, M]
]

### --- Read the topology, and generate all edges in the given topology.
edges = []
for i in range(len(M_topo)):
    for j in range(len(M_topo[0])):
        if i != j and M_topo[i][j] != M:
            edges.append((i, j, M_topo[i][j]))  ### (i,j) is a link; M_topo[i][j] here is 1, the length of link (i,j).

print("=== Dijkstra ===")
print("Let's find the shortest-path from 0 to 9:")
length,Shortest_path = dijkstra(edges, 0, 9)
print('length = ', length)
print('The shortest path is ', Shortest_path)
