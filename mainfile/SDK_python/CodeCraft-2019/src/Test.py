# 路口数组， 65 * 5
# 1，2，3，4列分别代表路口的上、右、下、左四个方向
cross = [
    [0, 0, 0, 0, 0],
    [1, 5000, 5007, -1, -1],
    [2, 5001, 5008, 5000, -1],
    [3, 5002, 5009, 5001, -1],
    [4, 5003, 5010, 5002, -1],
    [5, 5004, 5011, 5003, -1],
    [6, 5005, 5012, 5004, -1],
    [7, 5006, 5013, 5005, -1],
    [8, -1, 5014, 5006, -1],
    [9, 5015, 5022, -1, 5007],
    [10, 5016, 5023, 5015, 5008],
    [11, 5017, 5024, 5016, 5009],
    [12, 5018, 5025, 5017, 5010],
    [13, 5019, 5026, 5018, 5011],
    [14, 5020, 5027, 5019, 5012],
    [15, 5021, 5028, 5020, 5013],
    [16, -1, 5029, 5021, 5014],
    [17, 5030, 5035, -1, 5022],
    [18, -1, 5036, 5030, 5023],
    [19, 5031, 5037, -1, 5024],
    [20, 5032, 5038, 5031, 5025],
    [21, 5033, -1, 5032, 5026],
    [22, -1, 5039, 5033, 5027],
    [23, 5034, -1, -1, 5028],
    [24, -1, 5040, 5034, 5029],
    [25, 5041, 5048, -1, 5035],
    [26, 5042, 5049, 5041, 5036],
    [27, 5043, 5050, 5042, 5037],
    [28, 5044, 5051, 5043, 5038],
    [29, 5045, 5052, 5044, -1],
    [30, 5046, 5053, 5045, 5039],
    [31, 5047, 5054, 5046, -1],
    [32, -1, 5055, 5047, 5040],
    [33, 5056, 5062, -1, 5048],
    [34, 5057, 5063, 5056, 5049],
    [35, -1, 5064, 5057, 5050],
    [36, 5058, 5065, -1, 5051],
    [37, 5059, 5066, 5058, 5052],
    [38, 5060, 5067, 5059, 5053],
    [39, 5061, 5068, 5060, 5054],
    [40, -1, 5069, 5061, 5055],
    [41, 5070, 5077, -1, 5062],
    [42, 5071, 5078, 5070, 5063],
    [43, 5072, 5079, 5071, 5064],
    [44, 5073, 5080, 5072, 5065],
    [45, 5074, 5081, 5073, 5066],
    [46, 5075, 5082, 5074, 5067],
    [47, 5076, -1, 5075, 5068],
    [48, -1, 5083, 5076, 5069],
    [49, 5084, 5090, -1, 5077],
    [50, 5085, 5091, 5084, 5078],
    [51, 5086, 5092, 5085, 5079],
    [52, 5087, 5093, 5086, 5080],
    [53, -1, 5094, 5087, 5081],
    [54, 5088, 5095, -1, 5082],
    [55, 5089, 5096, 5088, -1],
    [56, -1, 5097, 5089, 5083],
    [57, 5098, -1, -1, 5090],
    [58, 5099, -1, 5098, 5091],
    [59, 5100, -1, 5099, 5092],
    [60, 5101, -1, 5100, 5093],
    [61, 5102, -1, 5101, 5094],
    [62, 5103, -1, 5102, 5095],
    [63, 5104, -1, 5103, 5096],
    [64, -1, -1, 5104, 5097]
]


# 维度
num = int((len(cross)-1)**0.5)

# 生成地图，左下角的路口设置为1
# a是二维数组，(num+1) * (num+1)

a = []

for i in range(num+1):
    new_arr = []
    for j in range(num+1):
        if i == num and j == 1:
            new_arr.append(1)
        else:
            new_arr.append(0)
    a.append(new_arr)


class C:
    def __init__(self, up, right, down, left):
        self.up = up
        self.right = right
        self.down = down
        self.left = left

    def is_up(self, c):
        if self.up == c.down and self.up != -1:
            return True
        else:
            return False

    def is_down(self, c):
        if self.down == c.up and self.down != -1:
            return True
        else:
            return False

    def is_right(self, c):
        if self.right == c.left and self.right != -1:
            return True
        else:
            return False

    def is_left(self, c):
        if self.left == c.right and self.left != -1:
            return True
        else:
            return False


# 存储路口对象
cross_obj_arr = []
for index in range(len(cross)):
    c = C(cross[index][1], cross[index][2], cross[index][3], cross[index][4])
    cross_obj_arr.append(c)


# 判断地图是否填满，行列从1开始
def if_a_not_full(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i][j] == 0:
                return True
    return False


# 输出地图的路口及连接的道路
def print_a_with_road(n):
    for i in range(1, n+1):
        print("           ")
        for j in range(1, n+1):
            print(a[i][j], end='\t')
            if cross_obj_arr[a[i][j]].right != -1:
                print("-", cross_obj_arr[a[i][j]].right, "-", end='\t')
            elif j != n:
                print("-0000- ", end="\t")
        print("")
        for k in range(1, n+1):
            if cross_obj_arr[a[i][k]].down != -1:
                print(cross_obj_arr[a[i][k]].down, end='\t')
            elif i != n:
                print("0000    ", end='\t')


while if_a_not_full(num):  # 当路口未填满时
    for i in range(1, num+1):
        for j in range(1, num+1):
            if a[i][j] != 0:  # 不为0说明该处由路口，根据这个路口找与其相连的路口
                # print(cross_obj_arr[a[i][j]].up)
                # print(cross_obj_arr[a[i][j]].right)
                # print(cross_obj_arr[a[i][j]].down)
                # print(cross_obj_arr[a[i][j]].left)

                for k in range(1, len(cross)):
                    if cross_obj_arr[a[i][j]].is_up(cross_obj_arr[k]):
                        a[i-1][j] = k
                    elif cross_obj_arr[a[i][j]].is_right(cross_obj_arr[k]):
                        a[i][j+1] = k
                    elif cross_obj_arr[a[i][j]].is_down(cross_obj_arr[k]):
                        a[i+1][j] = k
                    elif cross_obj_arr[a[i][j]].is_left(cross_obj_arr[k]):
                        a[i][j-1] = k

print_a_with_road(num)
