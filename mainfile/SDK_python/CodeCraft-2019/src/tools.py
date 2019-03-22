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
            car_str_list = [carstr.rstrip('\n') for carstr in car_str_list]
            # 逐个字符串处理
            for item in car_str_list[1:]:  # 第一个是注释不录入
                car_item_list = item[1:-1].replace(" ", "").split(',')  # 去除()和“ ”，以，分割
                car_id = car_item_list[0]
                dest_cross = car_item_list[1]
                orig_cross = car_item_list[2]
                limit_speed = int(car_item_list[3])
                start_time = int(car_item_list[4])
                temp_car = base_class.Car(car_id, dest_cross, orig_cross, limit_speed, start_time)
                car_list.append(temp_car)
        return car_list

    #将answerlist写入文件
    def  write_answer(self,answerlist:list):
        '''
        本函数需要按answerlist列表中的对象顺序依次写入路径为：answer_path(本类对象的属性：str)的文件。
        :param answerlist: 是一个answer对象列表
        :return: 返回是否写入成功
        '''
        pass


# t = Tools("../config_3/car.txt", "../config_3/road.txt", "../config_3/cross.txt", "../config_3/answer.txt")



for i in range(1,11):

    t = Tools("../config_"+str(i)+"/car.txt","../config_"+str(i)+"/road.txt","../config_"+str(i)+"/cross.txt","../config_"+str(i)+"/answer.txt")

    #test
    roadlist = t.read_road()
    crosses = t.read_cross()

    print("---------")
    print(len(roadlist))
    print(len(crosses))
    print("---------")
# print(roadlist[1])
# print(roadlist[0].road_len)
# print(roadlist[0].limit_speed)
# print(t.read_cross())
# print(t.read_car())

# roads = t.read_road()
# crosses = t.read_cross()
# res = base_class.RoadCrossMap(roads, crosses)
# roads_list = res.find_road_of_cross("2")
# print(roads_list)
#
# crosses_list = res.find_cross_of_road("5001")
# print(crosses_list)
