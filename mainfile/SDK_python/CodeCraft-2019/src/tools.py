'''
    工具类模块：
        输入文件转换成对应的数据结构、如将car.txt转换成car对象列表
'''

import base_class

class Tools():

    #初始化输入文件路径
    def __init__(self,car_path:str,road_path:str,cross_path:str,answer_path:str):
        self.car_path = car_path
        self.road_path = road_path
        self.cross_path = cross_path
        self.answer_path = answer_path

    #将road文件内容读入，并转换成对象列表
    def read_road(self):

        roadlist = []

        with open(self.road_path,'r') as f:
            road_str_list = f.readlines()

        if road_str_list:
            #去除换行符
            road_str_list = [roadstr.rstrip('\n') for roadstr in road_str_list]
            #逐个字符串处理
            for item in road_str_list[1:]:
                road_item_list = item[1:-1].replace(" ","").split(',')
                roadId = road_item_list[0]
                roadLen = int(road_item_list[1])
                limitSpeed = int(road_item_list[2])
                lane:int = int(road_item_list[3])
                origId:str = road_item_list[4]
                destId:str = road_item_list[5]
                is_dual:bool = True if road_item_list[6] else False
                temproad  = base_class.RoadWay(roadId, roadLen,limitSpeed,lane,origId,destId,is_dual)
                roadlist.append(temproad)

        return roadlist


    #将cross文件内容读入，并转换成对象列表
    def read_cross(self):
        pass

    #将car文件内容读入，并转换成对象列表
    def read_car(self):
        pass

    def __repr__(self):
        return '''This is object of tools:+
        ''' + dir(self)

    def __str__(self):
        return "This is object of tools"

t = Tools("../config/car.txt","../config/road.txt","../config/cross.txt","../config/answer.txt")

print(t.read_road())