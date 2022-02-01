for _ in range(4):
    data = list(map(int, input().split()))
    point_1 = [[data[0], data[1]], [data[2], data[1]], [data[2], data[3]], [data[0], data[3]]]
    point_2 = [[data[4], data[5]], [data[6], data[5]], [data[6], data[7]], [data[4], data[7]]]

    point_2_temp = point_2[2:] + point_2[:2]

    print(point_1)
    print(point_2)
    print(point_2_temp)
    for i in range(len(point_1)):
        switch = 0
        bool_1 = (point_1[i][0] > point_2_temp[i][0])
        bool_2 = (point_1[i][0] < point_2_temp[i][0])
        bool_3 = (point_1[i][1] > point_2_temp[i][1])
        bool_4 = (point_1[i][1] < point_2_temp[i][1])

        for j in range(len(point_1)):
            if point_1[j] == point_2_temp[j]:
                print('c')
                switch = 1
                break
        if switch == 1:
            break

        if ((i == 0 or i == 3) and bool_1) or ((i == 0 or i == 1) and bool_3) \
                or ((i == 1 or i == 2) and bool_2) or ((i == 2 or i == 3) and bool_4):
            print('d')
            break
        elif (point_1[i][0] == point_2_temp[i][0]) or (point_1[i][1] == point_2_temp[i][1]):
            print('b')
            break
        else:
            if i == len(point_1) - 1:
                print('a')
                break
            continue
