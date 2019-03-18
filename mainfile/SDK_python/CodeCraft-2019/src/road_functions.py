import tools


t = tools.Tools("../config/car.txt", "../config/road.txt", "../config/cross.txt", "../config/answer.txt")
road_list = t.read_road()
cross_list = t.read_cross()
# print(road_list[1].road_id)
# for road1 in road_list:
#     print(road1.road_id)
#     print(road1.orig_id)
#     print(road1.dest_id)


def find_cross_of_road(road_id):
    """
    输入1个Road的id，输出与该Road连接的2个Cross的id（必定是2个）
    结果存放于findCrossResult数组中，数组内值即为Cross的id
    :param road_id: 道路id
    :return: find_cross_result
    """
    find_cross_result = []
    for road_item in road_list:
        if int(road_item.road_id) == road_id:
            find_cross_result.append(int(road_item.orig_id))
            find_cross_result.append(int(road_item.dest_id))
    return find_cross_result


def find_road_of_cross(cross_id):
    """
    输入1个Cross的id，输出与该Cross相连接的1至4个Road的id（数量不定）
    结果存放于findRoadResult数组中

    不考虑单行的情况
    :param cross_id: 路口id
    :return: findRoadResult 与路口相邻的road
    """
    find_road_result = []
    for cross_item in cross_list:
        if int(cross_item.cross_id) == cross_id:
            cross_roads = cross_item.road_list
            for cross_roads_item in cross_roads:
                if int(cross_roads_item)!= -1:
                    find_road_result.append(int(cross_roads_item))
    return find_road_result


def beside_cross_of_cross(cross_id):
    """
    输入Cross的id，输出与该Cross相邻的1~4个Cross的id（数量不定）
    结果存放于BesideCrossRusult数组中，数组内值即为Cross的id，

    不考虑单行的情况
    :param cross_id: 路口id
    :return: BesideCrossRusult 与路口相邻的路口
    """
    get_road_list_of_cross = find_road_of_cross(cross_id)
    pass


# print(find_cross_of_road(5000))
# print(find_road_of_cross(2))
