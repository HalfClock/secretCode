"""
    工具类模块：
        输入文件转换成对应的数据结构、如将car.txt转换成car对象列表
"""
import time
from collections import defaultdict
from heapq import heappop, heappush

import base_class


class Tools(object):

    passtime = 1

    # 初始化输入文件路径
    def __init__(self, car_path: str, road_path: str, cross_path: str, answer_path: str):
        self.car_path = car_path
        self.road_path = road_path
        self.cross_path = cross_path
        self.answer_path = answer_path

    def __repr__(self):
        return '''This is object of tools:+
        ''' + dir(self)

    def __str__(self):
        return "This is object of tools"

    # 将road文件内容读入，并转换成对象列表
    def read_road(self):

        road_list = []

        with open(self.road_path, 'r') as f:
            road_str_list = f.readlines()

        if road_str_list:
            # 去除换行符
            road_str_list = [road_str.rstrip('\n') for road_str in road_str_list]
            # 逐个字符串处理
            for item in road_str_list[1:]:  # 第一个是注释不录入
                road_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                road_id = road_item_list[0]
                road_len = int(road_item_list[1])
                limit_speed = int(road_item_list[2])
                lane = int(road_item_list[3])
                orig_id = road_item_list[4]
                dest_id = road_item_list[5]
                is_dual = True if road_item_list[6] == "1" else False
                temp_road = base_class.RoadWay(road_id, road_len, limit_speed, lane, orig_id, dest_id, is_dual)
                road_list.append(temp_road)
        return road_list

    # 将cross文件内容读入，并转换成对象列表
    def read_cross(self):

        cross_list = []

        with open(self.cross_path, 'r') as f:
            cross_str_list = f.readlines()

        if cross_str_list:
            # 去除换行符
            cross_str_list = [cross_str.rstrip('\n') for cross_str in cross_str_list]
            # 逐个字符串处理
            for item in cross_str_list[1:]:  # 第一个是注释不录入
                cross_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                temp_cross = base_class.CrossRoads(cross_item_list[0], cross_item_list[1:])
                cross_list.append(temp_cross)
        return cross_list

    # 将car文件内容读入，并转换成对象列表
    def read_car(self):
        car_list = []

        with open(self.car_path, 'r') as f:
            car_str_list = f.readlines()

        if car_str_list:
            # 去除换行符
            car_str_list = [car_str.rstrip('\n') for car_str in car_str_list]
            # 逐个字符串处理
            for item in car_str_list[1:]:  # 第一个是注释不录入
                car_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                car_id = car_item_list[0]
                orig_cross = car_item_list[1]
                dest_cross = car_item_list[2]
                limit_speed = int(car_item_list[3])
                start_time = int(car_item_list[4])
                temp_car = base_class.Car(car_id, orig_cross,dest_cross,limit_speed, start_time)
                car_list.append(temp_car)
        return car_list


    # 获取所有的车速列表
    #没必要,可以直接用get_diff_speed_car_list返回的dict获取speedlist
    '''
    def get_car_speed_list(self,car_list):
        """
        :return: 所有车速
        """
        car_speed_list = set()
        for car in car_list:
            car_speed_list.add(car.limit_speed)
        return list(car_speed_list)
    '''

    #输入所有车辆列表、返回按车速不同分类的车辆的列表
    def get_diff_speed_car_dict(self,car_list):
        """
        :return diff_speed_car_dict:
        """
        diff_speed_car_dict = defaultdict(list)
        for car in car_list:
            diff_speed_car_dict[car.limit_speed].append(car)

        return diff_speed_car_dict

    #将一个列表里的车按照不同的源路口分类
    def classify_of_diff_ori_car(self,car_list):
        """

        :param carlist:
        :return:list[list]  第二维的每一个list
        :return:diff_ori_car_dict  第二维的每一个list的车源路口都不同
        """

        diff_ori_car_dict = defaultdict(list)

        for car in car_list:
            diff_ori_car_dict[car.orig_cross].append(car)

        return diff_ori_car_dict


    #dijkstra算法，获取单源点到多终点的最短路，并返回最短路字典
    def dijkstra_raw(self,edges, from_node, to_node_list):
        """

        :param edges: 边集 ——（路头，路尾，权值）
        :param from_node:源点
        :param to_node_list:终点
        :return: shortest_path_dict:最短路的字典 {key = to_node : value = (cost,path)}
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
                if v1 in to_node_list:  # 如果找到了某一个终点
                    shortest_path_dict[v1] = (cost, path)
                if len(shortest_path_dict) == len(to_node_list):  # 如果所有的tonode都找到了
                    return shortest_path_dict
                for c, v2 in g.get(v1, ()):  # 更新优先队列，加入与当前点相连的所有点的信息
                    if v2 not in seen:
                        heappush(q, (cost + c, v2, path))

        return {"ERROR": (float("inf"), [])}


    #解析最短路元组
    def tranfer_exp(self,length, path_queue):
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


    #给定速度的边集，和该速度的所有车辆对象，返回答案列表

    def dijkstra(self,edges, same_speed_car_list,rcmap):
        """

        :param edges: 该速度的地图边集 ——（路头，路尾，权值）
        :param same_speed_car_list: 一个Car类型对象的list、他们的车速都相同
        :param 传入一个地图对象用作生成roadlist
        :return: answer_list:答案对象列表、列表里是same_speed_car_list里每一辆车的最短路径答案
        """

        #初始化答案对象列表
        answer_list = []

        #将same_speed_car_list以不同的源路口进行分类
        diff_ori_car_dict = self.classify_of_diff_ori_car(same_speed_car_list)

        #针对不同源路口的车调用dijkstra算法
        for from_node,car_list in diff_ori_car_dict.items():

            #初始化终点集
            to_node_set = set()

            #对于相同的源ori_id提取不同的终点列表
            for car in car_list:
                to_node_set.add(car.dest_cross)
            to_node_list = list(to_node_set)

            #利用dijkstra_raw返回最短路的字典，{key = to_node : value = path}
            shortest_path_dict = self.dijkstra_raw(edges,from_node,to_node_list)

            #针对每一个终点生成最短路径列表
            for to_node,shortest_path in shortest_path_dict.items():

                #获取最短路(最短调度时间)，最短路的列表
                shortpathtime,path_list = self.tranfer_exp(shortest_path[0],shortest_path[1])


                #针对相同源id的车,如果目的地相同，那么就可以生成答案了
                for car in car_list:
                    if eval(car.dest_cross) == eval(to_node):
                        car_id = car.car_id #答案对象的car_id
                        road_id_list = rcmap.transfer_cross_to_road(path_list) #答案对象的path_list

                        start_time = self.compute_start_time_of_car(car,shortpathtime)  # 答案对象的start_time

                        # road_id_list = path_list
                        answer = base_class.Answer(car_id,start_time,road_id_list)
                        answer_list.append(answer)

        return answer_list


    #计算车的实际运行时间
    def compute_start_time_of_car(self,car,shortpathtime):
        """
        :param 当前的车对象
        :param shortpathtime: 该车到终点的最短运行时间
        :return: starttime:该车的实际出发时间
        """
        starttime = 1
        if car.start_time > Tools.passtime:#如果计划出发时间大于实际出发时间
            Tools.passtime = car.start_time

        starttime = Tools.passtime
        Tools.passtime += shortpathtime #全局时间推迟一辆车的运行时间

        return starttime




    # 将answer_list写入文件
    def write_answer(self, answer_list: list):
        """
        本函数需要按answer_list列表中的对象顺序依次写入路径为：
        answer_path(本类对象的属性：str)的文件。
        :param answer_list: 是一个answer对象列表
        :return: 返回是否写入成功

        """
        answer_path = self.answer_path
        with open(answer_path, 'w', encoding="utf-8") as f:
            for answer in answer_list:
                f.write(str(answer) + "\n")



# ---------------------------------------- test ----------------------------------------

# t = Tools("../config_3/car.txt", "../config_3/road.txt", "../config_3/cross.txt", "../config_3/answer.txt")


# for i in range(1, 11):
#     t = Tools("../config_" + str(i) + "/car.txt", "../config_" + str(i) + "/road.txt",
#               "../config_" + str(i) + "/cross.txt", "../config_" + str(i) + "/answer.txt")
#
#     # test
#     roadlist = t.read_road()
#     crosses = t.read_cross()
#
#     print("---------")
#     print(len(roadlist))
#     print(len(crosses))
#     print("---------")

# t = Tools("../config/car.txt",
#           "../config/road.txt",
#           "../config/cross.txt",
#           "../config/answer.txt")

# r = t.read_road()
# c = t.read_cross()
# s = t.get_car_speed_list()
# # print(r)
# # print(c)
# # print(s)
# rcm = base_class.RoadCrossMap(r, c, s)
# speed_dict = rcm.init_map_of_diff_speed(s)
# print(speed_dict)

"""
# ---------------------------------------- answer test ----------------------------------------
answer1 = base_class.Answer("1", 1, ["502", "506"])
answer2 = base_class.Answer("2", 2, ["503", "504", "505"])
answer3 = base_class.Answer("3", 3, ["501", "502"])
answers_list = [answer1, answer2, answer3]
t.write_answer(answers_list)

"""

#
# start = time.time()
#
# tool = Tools("../1-map-training-1/car.txt",
#           "../1-map-training-1/road.txt",
#           "../1-map-training-1/cross.txt",
#           "../1-map-training-1/answer.txt")
#
#
# #读各种数据
# road_list = tool.read_road()
# cross_list = tool.read_cross()
# carlist = tool.read_car()
#
# #获取不同速度车的字典
# diff_speed_car_dict = tool.get_diff_speed_car_dict(carlist)
#
# #获取速度列表
# diff_speed_list = list(diff_speed_car_dict.keys())
#
# #新建一个地图类
# rcMap_test = base_class.RoadCrossMap(road_list, cross_list, diff_speed_list)
#
# #获取不同速度的地图
# speed_dict = rcMap_test.init_map_of_diff_speed(diff_speed_list)
#
# all_answer_list = []
#
# #对于每一种速度生成的地图而言
# for speed,edges in speed_dict.items():
#
#     #获取相同速度车字典
#     same_speed_car_list = diff_speed_car_dict[speed]
#
#     #针对相同速度的车生成答案列表
#     answerlist = tool.dijkstra(edges, same_speed_car_list,rcMap_test)
#
#     #增加到所有的文件列表后
#     all_answer_list += answerlist
#
# print(all_answer_list)
#
# tool.write_answer(all_answer_list)
#
# end = time.time()
#
# print('Running time: %s Seconds'%(end-start))

