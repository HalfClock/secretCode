import math
import random
from collections import defaultdict
from heapq import *
import time

def dijkstra_raw_0(edges, from_node, to_node):
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


def dijkstra_raw(edges, from_node, to_node_list):
    """

    :param edges: 边集 ——（路头，路尾，权值）
    :param from_node:源点
    :param to_node_list:终点
    :return: shortest_path_dict:最短路的字典 {key = to_node : value = path}
    """

    shortest_path_dict = {}

    g = defaultdict(list)  # 定义一个空字典、此字典若没找到key，则返回空列表[]
    for l, r, c in edges:  # l:源点、r:终点 c:距离
        g[l].append((c, r))  # 建立一个字典，元素是源点为key、（距离，终点）为value

    q, seen = [(0, from_node, ())], set()  # 初始化优先队列、初始化已找到的最短路径集合——————元组（源点到点A的距离，某个点A，源点到点A的路径）
    while q:  # 优先队列为空时，循环结束
        (cost, v1, path) = heappop(q)  # 从优先队列中找出与源点距离最小的点
        if v1 not in seen:  # 若点v1以确定最短路径则无需计算
            seen.add(v1)
            path = (v1, path)
            if v1 in to_node_list: #如果找到了某一个终点
                shortest_path_dict[v1] = (cost,path)
            if len(shortest_path_dict) == len(to_node_list):#如果所有的tonode都找到了
                return shortest_path_dict
            for c, v2 in g.get(v1, ()):  # 更新优先队列，加入与当前点相连的所有点的信息
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return {"ERROR" :(float("inf"), [])}



def tranfer_exp(length,path_queue):
    len_shortest_path = -1
    ret_path = []
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. 拿到最短路;
        ## 2. 逐步从元组里拿到最短路径
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 记录终点
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 记录其他的点
            right = right[1]
        ret_path.reverse()  ## 3. 让输出的path为正向
    return len_shortest_path, ret_path


def dijkstra(edges, same_speed_car_list):
    """

    :param edges: 该速度的地图边集 ——（路头，路尾，权值）
    :param same_speed_car_list: 一个Car类型对象的list、他们的车速都相同
    :return: answer_list:答案对象列表、列表里是same_speed_car_list里每一辆车的最短路径答案
    """

    pass


def compute_cross_priority(cross_location_matrix):
    """
    这个函数假设路口位置矩阵是一个方阵
    :param cross_location_matrix: 路口位置矩阵
    :return: 路口优先级字典：{key = 路口id，value = (层级数，优先级数)}
    """

    #确定有多少层级
    lens = len(cross_location_matrix)
    layers_num =  math.ceil(float(len(cross_location_matrix))/2)

    cross_priority_dict = {}

    for layer in range(0,layers_num):
        count = 0
        for j in range(layer,lens-layer):

            cross_priority_dict[cross_location_matrix[layer][j]] = (layer,count)
            cross_priority_dict[cross_location_matrix[lens-layer -1][lens - j -1]] = (layer,count)
            count+=1

        for i in range(layer + 1,lens - layer -1):

            cross_priority_dict[cross_location_matrix[i][lens - layer -1]] = (layer,count)
            cross_priority_dict[cross_location_matrix[lens - i -1][layer]] = (layer,count)
            count+=1

    return cross_priority_dict


"""

# ---------------------------------------- test dijkstra ----------------------------------------

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



mat_len = 10

M_topo = [[random.choice(list(range(1,10))+[M]) for j in range(0, mat_len)] for i in range(0, mat_len)]


### --- Read the topology, and generate all edges in the given topology.
edges = []
for i in range(len(M_topo)):
    for j in range(len(M_topo[0])):
        if i != j and M_topo[i][j] != M:
            edges.append((i, j, M_topo[i][j]))  ### (i,j) is a link; M_topo[i][j] here is 1, the length of link (i,j).



print("原始dijkstra")
print("------------------")
start  = time.time()
for i in range(1,len(M_topo)):
    length,path_queue = dijkstra_raw_0(edges, 0, i)
    print(tranfer_exp(length,path_queue))

end = time.time()
print('Running time: %s Seconds'%(end-start))
print("------------------")



print("修改的dijkstra")
print("------------------")
start  = time.time()
returndict = dijkstra_raw(edges, 0, range(1,len(M_topo)))
for item in returndict.values():
    print(tranfer_exp(item[0],item[1]))
end = time.time()
print('Running time: %s Seconds'%(end-start))
print("------------------")

"""

# ---------------------------------------- test 设置优先级 ----------------------------------------

cross_location_matrix = [[i+j*8 for i in range(1,9)] for j in range(8)]

print(compute_cross_priority(cross_location_matrix))





