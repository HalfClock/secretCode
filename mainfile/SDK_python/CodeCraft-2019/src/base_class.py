'''
    基础类的模块
    基础类有：
        1、RoadWay 道路类
        2、CrossRoads 路口类
        3、Car 车类
        4、rcMap 地图类
        5、Answer 回答类
'''

#道路类
class RoadWay():
    
    def __init__(self, roadId:str=None, roadLen:int=None,limitSpeed:int=None,lane:int=None,origId:str=None,destId:str=None,is_dual:bool = False):
        self.road_id = roadId #道路id
        self.road_len = roadLen #道路长度
        self.limit_speed = limitSpeed #最高限速
        self.lane = lane #车道数目
        self.orig_id = origId #起始点id
        self.dest_id = destId #终点id
        self.isdual = is_dual #是否双向

    def __str__(self)->str:
        return "This is the road numbered " + self.road_id

    def __repr__(self)->str:
        return self.road_id

        
#路口类
class CrossRoads():
    def __init__(self, crossId:str = None, roadList:list = [None,None,None,None]):
        self.cross_id = crossId #节点id
        self.road_list = roadList #路口连接的道路

    def __str__(self)->str:
        return "This is the crossroad numbered " + self.cross_id

    def __repr__(self) -> str:
        return self.cross_id


#车类
class Car():
    def __init__(self, carId:str=None, destCross:str=None, origCross:str=None, limitSpeed:int=None, startTime:int=None):
        self.car_id = carId #车id
        self.dest_cross = destCross #目的路口id
        self.orig_cross = origCross #始发地路口id
        self.limit_speed = limitSpeed #车允许的最高速
        self.start_time = startTime #出发时间

    def __str__(self)->str:
        return "This id of this car is "+self.car_id

    def __repr__(self)->str:
        return self.car_id

#地图类
class rcMap():
    def __init__(self, roadList:list=None,crossList:list=None):

        #将列表转换成字典对象，该字典对象，key是id，值是对对应的对象，方便后面查找
        self.road_dict = {road.road_id : road for road in roadList}  #道路字典，key是id，值是id对应的道路对象
        self.cross_dict = {cross.cross_id : cross for cross in crossList}  #路口字典，key是id，值是id对应的路口对象

    def __repr__(self)->str:

        return '''This map contains all the roads and junctions,
include road:
             ''' + str([road for road in self.road_dict.keys()]) + '''
include cross:
             ''' + str([cross for cross in self.cross_dict.keys()])


#答案类
class Answer():
    def __init__(self, carId:str=None, startTime:int=None, roadIdList:list=None):
        self.car_id = carId #车id
        self.start_time = startTime #出发时间
        self.road_id_list = roadIdList #通过道路列表

    def __str__(self)->str:
        return '''The car with id ''' + self.car_id + ''' passes the road of ''' + str([roadid for roadid in self.road_id_list]) + " to reach the end."

    def __repr__(self)->str:
        return "This the answer of " + self.car_id +"car."



#test
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
# ans = Answer("1001",1,[1,2,3,4])
# print(ans)
#
# map = rcMap([r,r1],[c,c1])
# print(map)
