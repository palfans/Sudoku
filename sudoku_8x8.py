default_data = [[3, 6, 0, 0, 0, 0, 0, 2], 
                [0, 0, 2, 0, 0, 1, 0, 6],
                [0, 5, 8, 0, 0, 4, 3, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 4, 5, 0, 0, 7, 6, 0],
                [8, 0, 1, 0, 0, 2, 0, 0], 
                [2, 0, 0, 0, 0, 0, 8, 5]]

def print_sudoku(data):  #打印结果
    for i in range(8):
        for j in range(8):
            print('{:^2}'.format(data[i][j]), end='')
        print('')


def build_data_list(data):  #初始化
    data_list = []
    for y in range(8):
        for x in range(8):
            if data[y][x] == 0:
                data_list.append([(x, y), [1, 2, 3, 4, 5, 6, 7, 8]])
    return data_list


def judge(data, x, y, num):  #判断数字是否重复
    if data[y].count(num) > 0:  #行判断
        return False

    for col in range(8):  #列判断
        if data[col][x] == num:
            return False

    for a in range(2):  #宫判断
        for b in range(4):
            z1 = a + 2 * (y // 2)
            z2 = b + 4 * (x // 4) 
            z3 = data[a + 2 * (y // 2)][b + 4 * (x // 4)]
            if data[a + 2 * (y // 2)][b + 4 * (x // 4)] == num:
                return False
    return True


def data_list_filter(data, data_list, start):
    for blank_index in range(start, len(data_list)):
        data_list[blank_index][1] = []
        for num in range(1, 9):
            if judge(data, data_list[blank_index][0][0],
                     data_list[blank_index][0][1], num):
                data_list[blank_index][1].append(num)
    return data_list


def fill_num(
        data, data_list, start
):  #深度优先遍历
    if start < len(data_list):
        one = data_list[start]
        for num in one[1]:
            if judge(data, one[0][0], one[0][1], num):
                data[one[0][1]][one[0][0]] = num
                tem_data = fill_num(data, data_list, start + 1)
                if tem_data != None:
                    return tem_data
        data[one[0][1]][one[0][0]] = 0  #清零。
    else:
        return data


def main():  #主函数
    try:
        data = default_data
        print_sudoku(data)
        data_list = data_list_filter(data, build_data_list(data), 0)
        newdata = fill_num(data, data_list, 0)
        print('Answer:')
        print_sudoku(newdata)
    except Exception as e:
        print('Error occurred! please check your data~')
        print(str(e))


main()