for _ in range(4):
    data = list(map(int, input().split()))
    point_1 = [[data[0], data[1]], [data[2], data[1]], [data[2], data[3]], [data[0], data[3]]]
    point_2 = [[data[4], data[5]], [data[6], data[5]], [data[6], data[7]], [data[4], data[7]]]

    point_2_temp = point_2[2:] + point_2[:2]

    switch = 0

    for j in range(4):
        if point_1[j] == point_2_temp[j]:
            print('c')
            switch = 1
            break
    if switch == 1:
        continue

    for j in range(0, 4, 2):
        if (j == 0) and ((point_1[j][0] > point_2_temp[j][0]) or (point_1[j][1] > point_2_temp[j][1])):
            print('d')
            switch = 1
            break
        elif (j == 2) and ((point_1[j][0] < point_2_temp[j][0]) or (point_1[j][1] < point_2_temp[j][1])):
            print('d')
            switch = 1
            break
        else:
            continue
    if switch == 1:
        continue

    for j in range(4):
        if (point_1[j][0] == point_2_temp[j][0]) or (point_1[j][1] == point_2_temp[j][1]):
            print('b')
            switch = 1
            break
    if switch == 1:
        continue
    print('a')