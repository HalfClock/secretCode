"""
    基础类的模块
    基础类有：
        1、RoadWay 道路类
        2、CrossRoads 路口类
        3、Car 车类
        4、rcMap 地图类
        5、Answer 回答类
"""


# 道路类
class RoadWay(object):

    def __init__(self, road_id: str = None, road_len: int = None, limit_speed: int = None, lane: int = None,
                 orig_id: str = None, dest_id: str = None, is_dual: bool = False):
        self.road_id = road_id  # 道路id
        self.road_len = road_len  # 道路长度
        self.limit_speed = limit_speed  # 最高限速
        self.lane = lane  # 车道数目
        self.orig_id = orig_id  # 起始点id
        self.dest_id = dest_id  # 终点id
        self.is_dual = is_dual  # 是否双向

    def __str__(self) -> str:
        return "This is the road numbered " + str(self.road_id)

    def __repr__(self) -> str:
        return str(self.road_id)


# 路口类
class CrossRoads(object):
    def __init__(self, cross_id: str = None, road_list: list = None):
        self.cross_id = cross_id  # 节点id
        self.road_list = road_list  # 路口连接的道路

    def __str__(self) -> str:
        return "This is the crossroad numbered " + str(self.cross_id)

    def __repr__(self) -> str:
        return str(self.cross_id)


# 车类
class Car(object):
    def __init__(self, car_id: str = None, orig_cross: str = None, dest_cross: str = None, limit_speed: int = None,
                 start_time: int = None):
        self.car_id = car_id  # 车id
        self.dest_cross = dest_cross  # 目的路口id
        self.orig_cross = orig_cross  # 始发地路口id
        self.limit_speed = limit_speed  # 车允许的最高速
        self.start_time = start_time  # 出发时间

    def __str__(self) -> str:
        return "This id of this car is " + str(self.car_id)

    def __repr__(self) -> str:
        return str(self.car_id)


# 地图类
class RoadCrossMap(object):
    def __init__(self, road_list: list = None, cross_list: list = None, car_speed_list: list = None):
        # 将列表转换成字典对象，该字典对象，key是id，值是对对应的对象，方便后面查找
        self.road_dict = {road.road_id: road for road in road_list}  # 道路字典，key是id，值是id对应的道路对象
        self.cross_dict = {cross.cross_id: cross for cross in cross_list}  # 路口字典，key是id，值是id对应的路口对象
        self.map_dict = self.init_map_of_diff_speed(car_speed_list)  # 根据不同车的速度生成的地图索引

    def __repr__(self) -> str:
        return '''This map contains all the roads and junctions,
include road:
             ''' + str([road for road in self.road_dict.keys()]) + '''
include cross:
             ''' + str([cross for cross in self.cross_dict.keys()])

    def find_cross_of_road(self, road_id):
        """
        输入1个Road的id，输出与该Road连接的2个Cross的id（必定是2个）
        结果存放于findCrossResult数组中，数组内值即为Cross的id
        :param road_id: 道路id
        :return: find_cross_result
        """
        find_cross_result = []
        road_obj = self.road_dict[road_id]
        find_cross_result.append(road_obj.orig_id)
        find_cross_result.append(road_obj.dest_id)
        return find_cross_result

    def find_road_of_cross(self, cross_id):
        """
        输入1个Cross的id，输出与该Cross相连接的1至4个Road的id（数量不定）
        结果存放于findRoadResult数组中

        不考虑单行的情况
        :param cross_id: 路口id
        :return: findRoadResult 与路口相邻的road
        """
        find_road_result = []
        cross_obj = self.cross_dict[cross_id]
        road_list = cross_obj.road_list
        for road_item in road_list:
            if str(road_item) != str(-1):
                find_road_result.append(road_item)
        return find_road_result

    """
        以下函数以本类的属性作为基础编写！！！！！
        
        注意！！！！！本类的属性是两个字典、分别是道路字典和路口字典
        
        道路字典：
           1、存放着本地图所有的RoadWay对象
           2、key 是RoadWay对象的id字符串
           3、value 是对应id的RoadWay对象
        
        路口字典：
            1、存放着本地图所有的CrossRoads对象
            2、key 是CrossRoads对象的id字符串
            3、value 是对应id的CrossRoads对象
        
        因为是字典、所以查找很快,很多查询不需要单独写函数：
            比如：
                找与road_id = 1001道路相连的2个Cross、就一行代码：
                (road_dict['1001'].orig_id,road_dict['1001'].destId)             
        
    """

    def beside_cross_of_cross(self, cross_id: str) -> list:
        """
        输入Cross的id，输出与该Cross相邻的1~4个Cross的id（数量不定）
        结果存放于BesideCrossRusult数组中，数组内值即为Cross的id字符串，

        不考虑单行的情况
        :param cross_id: 路口id
        :return: list[str]: BesideCrossRusult 与路口相邻的路口
        """
        beside_cross_result = []
        # 找到与这个路口相关联的road
        related_roads = self.find_road_of_cross(cross_id)
        for road_item in related_roads:
            beside_cross_result.extend(self.find_cross_of_road(road_item))
        beside_cross_result = list(set(beside_cross_result))
        beside_cross_result.remove(cross_id)
        return beside_cross_result

    def beside_road_of_road(self, road_id: str) -> list:
        """
        输入Road的id，输出与该Road相邻的1~6个Road的id（数量不定）
        结果存放于BesideRoadRusult数组中，数组内值即为Road的id，存在几个-1则说明该Road在最多6个相邻Road的基础上少几个
        BesideRoadRusult数组中的数据乱序，若存在-1则其所在位置随机
        不考虑单行的情况

        :param: road_id: 道路id
        :return: list[str] : BesideRoadRusult
        """
        beside_road_result = []
        # 找到与道路相关联的cross
        related_cross = self.find_cross_of_road(road_id)
        for cross_item in related_cross:
            beside_road_result.extend(self.find_road_of_cross(cross_item))
        beside_road_result = list(set(beside_road_result))
        beside_road_result.remove(road_id)
        return beside_road_result

    def is_cross_access(self, cross_id1: str, cross_id2: str) -> int:
        """
        Input 2 Corss id
        输入两个Cross的id(有先后顺序)，判断Cross1和Cross2是否相邻(或从Cross1到Cross2是否可达)
        输出为1说明相邻（即Cross1到Cross2之间有一条路）；
        输出为0则说明Cross1到Cross2之间有一个Road，但路是单行导致从Cross1到Cross2不能通过该Road可达；
        输出为-1说明Cross1到Cross2之间不存在一个Road相连接

        :param: Cross_id1:str 路口1的id, Cross_id2 :str 路口2的id
        :return: 1 / 0 / -1
        """
        road_dict = self.road_dict
        for road_item in road_dict.keys():
            road_obj = road_dict[road_item]
            if cross_id1 == road_obj.orig_id and cross_id2 == road_obj.dest_id:
                if road_obj.is_dual:
                    return 1
                else:
                    return 1
            elif cross_id1 == road_obj.dest_id and cross_id2 == road_obj.orig_id:
                if road_obj.is_dual:
                    return 1
                else:
                    return 0
        return -1

    # def is_road_access(self, road_id1: str, road_id2: str) -> int:
    #     """
    #         Input 2 Road id , Output ture/false 判断两个Road是否相邻，如果是单行则需要进一步判断
    #         输入两个Road的id(有先后顺序)，判断Road1和Road是否相邻(或可从Road1通过到Road2)
    #         输出为1说明相邻（即Road1和Road2连接同一个Cross）；
    #         输出为0则说明Road1和Road2连接同一个Cross，但Road1和Road2中存在有路是单行导致从Road1一端到该Cross再到Road2另一端不能通过；
    #         输出为-1说明Road1和Road2没有连接同一个Cross
    #
    #         :param: Road_id1:str 路口1的id, Road_id2 :str 路口2的id
    #         :return: 1 / 0 / -1
    #     """
    #     related_cross_of_road1 = self.find_cross_of_road(road_id1)
    #     related_cross_of_road2 = self.find_cross_of_road(road_id2)
    #     for cross_item1 in related_cross_of_road1:
    #         for cross_item2 in related_cross_of_road2:
    #             if cross_item1 != cross_item2:
    #                 pass
    #     pass

    # 输入两个路口的id，若两个路口相邻则返回连接两个路口的道路id，若无则返回-1
    def find_road_by_cross(self, cross_from, cross_to):
        """

        :param cross_from: 源路口id
        :param cross_to: 目的路口id
        :return: 道路id/-1
        """
        # 与源路口连接的道路id
        road_list = self.find_road_of_cross(cross_from)

        for roadid in road_list:
            road_obj = self.road_dict[roadid]

            if road_obj.is_dual:  # 如果道路是双向的、那么cross_to可能是这条路的源点也有可能是这条路的终点
                if (road_obj.dest_id == cross_to) or (road_obj.orig_id == cross_to):
                    return roadid
            elif not road_obj.is_dual:  # 如果这条路是单向的，那么cross_to只能是这条路的终点
                if road_obj.dest_id == cross_to:
                    return roadid

        return -1

    # 输入一个路口列表，其中相邻的两个路口必定是一个道路的源点和终点,返回两两连接的道路id列表，如果函数运行中发现不是，那么返回-1
    def transfer_cross_to_road(self, cross_list):
        """
        :param cross_list:
        :return: road_list
        """
        road_list = []

        for i in range(len(cross_list) - 1):

            road_id = self.find_road_by_cross(cross_list[i], cross_list[i + 1])
            if road_id == -1:
                return -1
            else:
                road_list.append(road_id)

        return road_list

    # 依据不同的车速生成不同的地图
    def init_map_of_diff_speed(self, car_speed_list):
        """
        :param car_speed_list: 这个列表里有各种车速
        :return:一个字典，这个字典的key是车速（int），value是对应速度生成的edges,这个edges是一个列表，
                元素是一个元组（源路口id，目的路口id，权值）
        例如：
        {4 : [(1,2,10),(2,3,18),(3,4,16),...] , 5 : [(1,2,9),(2,3,17),(3,4,16),...]}

        """

        road_dict = self.road_dict  # 拿到路字典
        speed_dict = {}  # 初始化结果字典

        for car_speed in car_speed_list:  # 对于每一种车速进行遍历

            for road in road_dict:  # 对于每一种测速遍历每一条路
                road_limit_speed = road_dict[road].limit_speed
                final_speed = min(road_limit_speed, car_speed)  # 拿到本车速的理论最高速

                if car_speed not in speed_dict:  # 差错控制
                    speed_dict[car_speed] = []

                if road_dict[road].is_dual:  # 如果路是双向

                    speed_dict[car_speed].append((road_dict[road].orig_id,
                                                  road_dict[road].dest_id,
                                                  road_dict[road].road_len // final_speed))
                    speed_dict[car_speed].append((road_dict[road].dest_id,
                                                  road_dict[road].orig_id,
                                                  road_dict[road].road_len // final_speed))
                else:  # 如果路是单向

                    speed_dict[car_speed].append((road_dict[road].orig_id,
                                                  road_dict[road].dest_id,
                                                  road_dict[road].road_len // final_speed))

        return speed_dict


# 答案类
class Answer(object):
    def __init__(self, car_id: str = None, start_time: int = None, road_id_list: list = None):
        self.car_id = car_id  # 车id
        self.start_time = start_time  # 出发时间
        self.road_id_list = road_id_list  # 通过道路列表

    def __str__(self) -> str:
        return str(tuple([eval(self.car_id), self.start_time] + [eval(roadid) for roadid in self.road_id_list]))

    def __repr__(self) -> str:
        return str(self)

# ---------------------------------------- test ----------------------------------------

# r = RoadWay("501",10,6,5,"1","2",True)
# r1 = RoadWay("502",10,6,5,"3","4",True)
# print(r)
#
#
# c = CrossRoads("1", ["501", "513", -1, -1])
# c1 = CrossRoads("2", ["502", "514", "555", -1])
# print(c)
#
#
# car = Car("1001","1","16",6,1)
# print(car)
#
#
# ans = Answer("1001",1,["1","2","3","4"])
# print(ans)
#
# map = rcMap([r,r1],[c,c1])
# print(map)
