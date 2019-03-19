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

    def __init__(self, roadId: str = None, roadLen: int = None, limitSpeed: int = None, lane: int = None,
                 origId: str = None, destId: str = None, is_dual: bool = False):
        self.road_id = roadId  # 道路id
        self.road_len = roadLen  # 道路长度
        self.limit_speed = limitSpeed  # 最高限速
        self.lane = lane  # 车道数目
        self.orig_id = origId  # 起始点id
        self.dest_id = destId  # 终点id
        self.isdual = is_dual  # 是否双向

    def __str__(self) -> str:
        return "This is the road numbered " + str(self.road_id)

    def __repr__(self) -> str:
        return str(self.road_id)


# 路口类
class CrossRoads(object):
    def __init__(self, crossId: str = None, roadList: list = [None, None, None, None]):
        self.cross_id = crossId  # 节点id
        self.road_list = roadList  # 路口连接的道路

    def __str__(self) -> str:
        return "This is the crossroad numbered " + str(self.cross_id)

    def __repr__(self) -> str:
        return str(self.cross_id)


# 车类
class Car(object):
    def __init__(self, carId: str = None, destCross: str = None, origCross: str = None, limitSpeed: int = None,
                 startTime: int = None):
        self.car_id = carId  # 车id
        self.dest_cross = destCross  # 目的路口id
        self.orig_cross = origCross  # 始发地路口id
        self.limit_speed = limitSpeed  # 车允许的最高速
        self.start_time = startTime  # 出发时间

    def __str__(self) -> str:
        return "This id of this car is " + str(self.car_id)

    def __repr__(self) -> str:
        return str(self.car_id)


# 地图类
class rcMap(object):
    def __init__(self, roadList: list = None, crossList: list = None):

        # 将列表转换成字典对象，该字典对象，key是id，值是对对应的对象，方便后面查找
        self.road_dict = {road.road_id: road for road in roadList}  # 道路字典，key是id，值是id对应的道路对象
        self.cross_dict = {cross.cross_id: cross for cross in crossList}  # 路口字典，key是id，值是id对应的路口对象

    def __repr__(self) -> str:
        return '''This map contains all the roads and junctions,
include road:
             ''' + str([road for road in self.road_dict.keys()]) + '''
include cross:
             ''' + str([cross for cross in self.cross_dict.keys()])


    '''
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
                    
        
    '''

    def beside_cross_of_cross(self,cross_id:str)->list:
        """
        输入Cross的id，输出与该Cross相邻的1~4个Cross的id（数量不定）
        结果存放于BesideCrossRusult数组中，数组内值即为Cross的id字符串，

        不考虑单行的情况
        :param cross_id: 路口id
        :return: list[str]: BesideCrossRusult 与路口相邻的路口
        """
        pass

    def Beside_road_of_road(self,road_id:str)->list:
        """
        输入Road的id，输出与该Road相邻的1~6个Road的id（数量不定）
        结果存放于BesideRoadRusult数组中，数组内值即为Road的id，存在几个-1则说明该Road在最多6个相邻Road的基础上少几个
        BesideRoadRusult数组中的数据乱序，若存在-1则其所在位置随机
        不考虑单行的情况

        :param: road_id: 道路id
        :return: list[str] : BesideRoadRusult
        """
        pass

    def isCrossAccess(self,Cross_id1:str, Cross_id2:str)-> int:

        """
        Input 2 Corss id
        输入两个Cross的id(有先后顺序)，判断Cross1和Cross2是否相邻(或从Cross1到Cross2是否可达)
        输出为1说明相邻（即Cross1到Cross2之间有一条路）；
        输出为0则说明Cross1到Cross2之间有一个Road，但路是单行导致从Cross1到Cross2不能通过该Road可达；
        输出为-1说明Cross1到Cross2之间不存在一个Road相连接

        :param: Cross_id1:str 路口1的id, Cross_id2 :str 路口2的id
        :return: 1 / 0 / -1
        """
        pass

    def isRoadAccess(Road_id1:str, Road_id2:str) -> int:
        """
            Input 2 Road id , Output ture/false 判断两个Road是否相邻，如果是单行则需要进一步判断
            输入两个Road的id(有先后顺序)，判断Road1和Road是否相邻(或可从Road1通过到Road2)
            输出为1说明相邻（即Road1和Road2连接同一个Cross）；
            输出为0则说明Road1和Road2连接同一个Cross，但Road1和Road2中存在有路是单行导致从Road1一端到该Cross再到Road2另一端不能通过；
            输出为-1说明Road1和Road2没有连接同一个Cross

            :param: Road_id1:str 路口1的id, Road_id2 :str 路口2的id
            :return: 1 / 0 / -1
        """
        pass





# 答案类
class Answer(object):
    def __init__(self, carId: str = None, startTime: int = None, roadIdList: list = None):
        self.car_id = carId  # 车id
        self.start_time = startTime  # 出发时间
        self.road_id_list = roadIdList  # 通过道路列表

    def __str__(self) -> str:

        return str(tuple([self.car_id,str(self.start_time)]+[roadid for roadid in self.road_id_list]))

    def __repr__(self) -> str:
        return str(self.car_id)

# test
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
