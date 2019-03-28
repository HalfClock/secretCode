import logging
import sys
import time

import tools
import base_class

logging.basicConfig(level=logging.DEBUG,
                    filename='../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


def main():
    if len(sys.argv) != 5:
        logging.info('please input args: car_path, road_path, cross_path, answerPath')
        exit(1)

    car_path = sys.argv[1]
    road_path = sys.argv[2]
    cross_path = sys.argv[3]
    answer_path = sys.argv[4]

    logging.info("car_path is %s" % (car_path))
    logging.info("road_path is %s" % (road_path))
    logging.info("cross_path is %s" % (cross_path))
    logging.info("answer_path is %s" % (answer_path))

# to read input file
# process
# to write output file
    start = time.time()
    tool = tools.Tools(car_path,
                 road_path,
                 cross_path,
                answer_path)

    # 读各种数据
    road_list = tool.read_road()
    cross_list = tool.read_cross()
    carlist = tool.read_car()

    # 获取不同速度车的字典
    diff_speed_car_dict = tool.get_diff_speed_car_dict(carlist)

    # 获取速度列表
    diff_speed_list = list(diff_speed_car_dict.keys())

    # 新建一个地图类
    rcMap_test = base_class.RoadCrossMap(road_list, cross_list, diff_speed_list)

    # 获取不同速度的地图
    speed_dict = rcMap_test.init_map_of_diff_speed(diff_speed_list)

    all_answer_list = []

    # 对于每一种速度生成的地图而言
    for speed, edges in speed_dict.items():
        # 获取相同速度车字典
        same_speed_car_list = diff_speed_car_dict[speed]

        # 针对相同速度的车生成答案列表
        answerlist = tool.dijkstra(edges, same_speed_car_list, rcMap_test,diff_speed_list)

        # 增加到所有的文件列表后
        all_answer_list += answerlist

    # print(all_answer_list)

    tool.write_answer(all_answer_list)

    end = time.time()

    logging.info('Running time: %s Seconds'%(end-start))

if __name__ == "__main__":
    main()