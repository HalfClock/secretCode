"""
    工具类模块：
        输入文件转换成对应的数据结构、如将car.txt转换成car对象列表
"""

import base_class


class Tools(object):

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

        roadlist = []

        with open(self.road_path, 'r') as f:
            road_str_list = f.readlines()

        if road_str_list:
            # 去除换行符
            road_str_list = [roadstr.rstrip('\n') for roadstr in road_str_list]
            # 逐个字符串处理
            for item in road_str_list[1:]:  # 第一个是注释不录入
                road_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                roadId = road_item_list[0]
                roadLen = int(road_item_list[1])
                limitSpeed = int(road_item_list[2])
                lane = int(road_item_list[3])
                origId = road_item_list[4]
                destId = road_item_list[5]
                is_dual = True if road_item_list[6] == "1" else False
                temproad  = base_class.RoadWay(roadId, roadLen,limitSpeed,lane,origId,destId,is_dual)
                roadlist.append(temproad)
        return roadlist

    # 将cross文件内容读入，并转换成对象列表
    def read_cross(self):

        crosslist = []

        with open(self.cross_path, 'r') as f:
            cross_str_list = f.readlines()

        if cross_str_list:
            # 去除换行符
            cross_str_list = [crossstr.rstrip('\n') for crossstr in cross_str_list]
            # 逐个字符串处理
            for item in cross_str_list[1:]:  # 第一个是注释不录入
                cross_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                tempcross = base_class.CrossRoads(cross_item_list[0], cross_item_list[1:])
                crosslist.append(tempcross)
        return crosslist

    # 将car文件内容读入，并转换成对象列表
    def read_car(self):
        carlist = []

        with open(self.car_path, 'r') as f:
            car_str_list = f.readlines()

        if car_str_list:
            # 去除换行符
            car_str_list = [carstr.rstrip('\n') for carstr in car_str_list]
            # 逐个字符串处理
            for item in car_str_list[1:]:  # 第一个是注释不录入
                car_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                carId = car_item_list[0]
                destCross = car_item_list[1]
                origCross = car_item_list[2]
                limitSpeed = int(car_item_list[3])
                startTime = int(car_item_list[4])
                tempcar = base_class.Car(carId, destCross, origCross, limitSpeed, startTime)
                carlist.append(tempcar)
        return carlist

    # #将carlist写入文件
    # def  write_car(self):



t = Tools("../config/car.txt", "../config/road.txt", "../config/cross.txt", "../config/answer.txt")


t = Tools("../config/car.txt","../config/road.txt","../config/cross.txt","../config/answer.txt")

#test
roadlist = t.read_road()
print(roadlist)
# print(roadlist[1])
# print(roadlist[0].road_len)
# print(roadlist[0].limit_speed)
# print(t.read_cross())
# print(t.read_car())

