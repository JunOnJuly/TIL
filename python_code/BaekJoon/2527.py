for _ in range(4):
    data = list(map(int, input().split()))

    points_1 = [[data[0], data[1]], [data[2], data[3]], [data[0], data[3]], [data[2], data[1]]]
    points_2 = [[data[4], data[5]], [data[6], data[7]], [data[4], data[7]], [data[6], data[5]]]

    for point in points_1:
        if point in points_2:
            print('c')