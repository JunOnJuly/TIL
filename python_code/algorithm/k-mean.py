# k-means clustering

import random as rd
import matplotlib.pyplot as plt
import math


# function makes random data for test
def make_random_points(point_num: int, x_limit: int, y_limit: int) -> list:
    """
    :param point_num: how much data is (0 < point_num <= (x_limit+1)*(y_limit+1))
    :param x_limit: maximum range of x (0 <= x <= x_limit)
    :param y_limit: maximun range of y (0 <= y <= y_limit)
    :return: three lists - x data, y data, index data
    """

    # x data to return
    points_x_list: list = []
    # y data to return
    points_y_list: list = []
    # index data to avoid duplication
    xy_list: list = []

    # count of data
    cnt: int = 0
    while True:
        # if number of data same as target number, stop add data
        if cnt == point_num:
            break
        # makes random data for test
        idx_random: list = [rd.randint(0, x_limit), rd.randint(0, y_limit)]
        # avoid duplication
        if idx_random not in xy_list:
            xy_list.append(idx_random)
        else:
            continue

        cnt += 1

    # sort list of data
    xy_list = sorted(xy_list, key=lambda idx: (abs(x_limit // 2 - idx[0]), abs(y_limit // 2 - idx[1])))

    # split index to easy use
    for i in range(point_num):
        points_x_list.append(xy_list[i][0])
        points_y_list.append(xy_list[i][1])

    return points_x_list, points_y_list, xy_list


# function makes clustering point
def make_random_clusters(cluster_num: int, x_limit: int, y_limit: int) -> list:
    """
    :param cluster_num: how much cluster is (0 < cluster_num <= 7)
    :param x_limit: maximum range of x (0 <= x <= x_limit)
    :param y_limit: maximum range of y (0 <= y <= y_limit)
    :return: three lists - x data, y data, index data
    """

    # x data to return
    cluster_x_list: list = []
    # y data to return
    cluster_y_list: list = []
    # index data to avoid duplication
    xy_list: list = []

    # count of cluster
    cnt: int = 0
    while True:
        # if number of cluster same as target number, stop add cluster
        if cnt == cluster_num:
            break
        # makes random cluster
        idx_random: list = [rd.randint(0, x_limit), rd.randint(0, y_limit)]

        # avoid duplication
        if idx_random not in xy_list:
            xy_list.append(idx_random)
        else:
            continue

        cnt += 1

    # split index to easy use
    for i in range(cluster_num):
        cluster_x_list.append(xy_list[i][0])
        cluster_y_list.append(xy_list[i][1])

    return cluster_x_list, cluster_y_list, xy_list


# calculate distance between cluster and data
def cal_dist(point1x: int, point1y: int, point2x: int, point2y: int) -> int:
    """
    :param point1x: x index of data
    :param point1y: y index of data
    :param point2x: x index of cluster
    :param point2y: y index of cluster
    :return: distance of cluster and data, xx.xxxxx
    """
    return round(((point1x - point2x) ** 2 + (point1y - point2y) ** 2) ** (1 / 2), 5)


# classify data with distance
def classify_data(point_num: int, cluster_num: int, point_list_x: list, point_list_y: list, cluster_list_x: list,
                  cluster_list_y: list) -> list:
    """
    :param point_num: how much data is
    :param cluster_num: how much cluster is
    :param point_list_x: x index of data
    :param point_list_y: y index of data
    :param cluster_list_x: x index of cluster
    :param cluster_list_y: y index of cluster
    :return: list of data classified
    """

    # list of data classified to return
    point_in_cluster: list = [[] for _ in range(cluster_num)]

    for i in range(point_num):
        # minimum distance
        min_dist: int = 1.5 * (point_num ** 2)
        # number of closest cluster
        selected_cluster: int = cluster_num
        for j in range(cluster_num):
            # distance between data and cluster
            to_cluster_dist: int = cal_dist(point_list_x[i], point_list_y[i], cluster_list_x[j], cluster_list_y[j])

            # find closest cluster
            if to_cluster_dist < min_dist:
                min_dist = to_cluster_dist
                selected_cluster = j
        point_in_cluster[selected_cluster].append(i)
    return point_in_cluster


# replace cluster to center of classified data
def replace_cluster(cluster_num: int, point_cluster_list: list, point_list_x: list, point_list_y: list) -> list:
    """
    :param cluster_num: how much cluster is
    :param point_cluster_list: list classified data
    :param point_list_x: x index of data
    :param point_list_y: y index of data
    :return: two lists - x data, y data
    """

    # x of replaced cluster
    cluster_list_x: list = []
    # y of replaced cluster
    cluster_list_y: list = []

    for i in range(cluster_num):
        # how much data is close with cluster
        length_cluster: int = len(point_cluster_list[i])
        if length_cluster == 0:
            cluster_list_x.append(X[i])
            cluster_list_y.append(Y[i])
            continue
        # sum of x
        sum_point_x: int = sum([point_list_x[point_cluster_list[i][j]] for j in range(length_cluster)])
        # sum of y
        sum_point_y: int = sum([point_list_y[point_cluster_list[i][j]] for j in range(length_cluster)])

        # add replaced cluster
        cluster_list_x.append(round(sum_point_x / length_cluster))
        cluster_list_y.append(round(sum_point_y / length_cluster))

    return cluster_list_x, cluster_list_y


# calculate degree
def calculate_degree(cluster_x: int, cluster_y: int, point_x: int, point_y: int) -> float:
    """
    :param cluster_x: x index of cluster
    :param cluster_y: y index of cluster
    :param point_x: x index of data
    :param point_y: y index of data
    :return: degree
    """

    if cluster_x == point_x:
        if cluster_y > point_y:
            return 180
        else:
            return 0

    elif cluster_y == point_y:
        if cluster_x > point_x:
            return 270
        else:
            return 90

    elif cluster_x < point_x and cluster_y < point_y:
        length_x = point_x - cluster_x
        length_y = point_y - cluster_y
        rad = math.atan2(length_y, length_x)
        deg = rad * 180 / math.pi
        return 90 - round(deg)

    elif cluster_x > point_x and cluster_y < point_y:
        length_x = cluster_x - point_x
        length_y = point_y - cluster_y
        rad = math.atan2(length_y, length_x)
        deg = rad * 180 / math.pi
        return 270 + round(deg)

    elif cluster_x > point_x and cluster_y > point_y:
        length_x = cluster_x - point_x
        length_y = cluster_y - point_y
        rad = math.atan2(length_y, length_x)
        deg = rad * 180 / math.pi
        return 270 - round(deg)

    elif cluster_x < point_x and cluster_y > point_y:
        length_x = point_x - cluster_x
        length_y = cluster_y - point_y
        rad = math.atan2(length_y, length_x)
        deg = rad * 180 / math.pi
        return 90 + round(deg)


# number of data
n: int = 1000
# limit of data
limitx: int = 1000
limity: int = 1000
# number of cluster
m: int = 5
# make test data
x, y, xy = make_random_points(n, limitx, limity)
# make init cluster
X, Y, XY = make_random_clusters(m, limitx, limity)

while True:
    # cluster data before
    X_pre = X[:]
    Y_pre = Y[:]
    # classify data with cluster
    classify_list: list = classify_data(n, m, x, y, X, Y)
    # replace cluster with classify data
    X, Y = replace_cluster(m, classify_list, x, y)
    # end if cluster is not changed
    if [X_pre, Y_pre] == [X, Y]:
        break

border_list = []
for i in range(m):
    cluster_data_list = []
    border_data_list = []
    for j in range(len(classify_list[i])):
        degree = calculate_degree(X[i], Y[i], x[classify_list[i][j]], y[classify_list[i][j]])
        distance = cal_dist(X[i], Y[i], x[classify_list[i][j]], y[classify_list[i][j]])
        cluster_data_list.append([degree, distance])

    pre_max = 100
    for j in range(0, 360):
        max_length = 0
        max_index = -1

        for k in range(len(cluster_data_list)):
            if cluster_data_list[k][0] == j:
                if max_length < cluster_data_list[k][1] and \
                        pre_max*0.6 < cluster_data_list[k][1]:
                    max_length = cluster_data_list[k][1]
                    max_index = k

        if max_index == -1:
            continue
        else:
            border_data_list.append(max_index)
            pre_max = max_length + 0
    border_list.append(border_data_list)

border_line_list = [[] for _ in range(m)]
for i in range(m):
    for j in range(len(border_list[i])):
        border_line_list[i].append(classify_list[i][border_list[i][j]])
    border_line_list[i].append(border_line_list[i][0])
# color guide of graph
plt_guide: list = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

for i in range(m):
    plt.plot([x[j] for j in classify_list[i]], [y[j] for j in classify_list[i]], f'{plt_guide[i]}.')
    plt.plot(X[i], Y[i], 'k^')
    plt.plot([x[j] for j in border_line_list[i]], [y[j] for j in border_line_list[i]], plt_guide[i])
plt.show()
