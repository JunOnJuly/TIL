# k-means clustering

import random as rd
import matplotlib.pyplot as plt


# function makes random data for test
def make_random_points(point_num: int, x_limit: int, y_limit: int) -> list:
    """
    :param point_num: how much data is (0 < point_num <= (x_limit+1)*(y_limit+1))
    :param x_limit: maximum range of x (0 <= x <= x_limit)
    :param y_limit: maximun range of y (0 <= y <= y_limit)
    :return: two lists - x data, y data
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

    # split index to easy use
    for i in range(point_num):
        points_x_list.append(xy_list[i][0])
        points_y_list.append(xy_list[i][1])

    return points_x_list, points_y_list


# function makes clustering point
def make_random_clusters(cluster_num: int, x_limit: int, y_limit: int) -> list:
    """
    :param cluster_num: how much cluster is (0 < cluster_num <= 7)
    :param x_limit: maximum range of x (0 <= x <= x_limit)
    :param y_limit: maximum range of y (0 <= y <= y_limit)
    :return: two lists - x data, y data
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

    return cluster_x_list, cluster_y_list


# calculate distance between cluster and data
def cal_dist(point1x: int, point1y: int, point2x: int, point2y: int) -> int:
    """
    :param point1x: x index of data
    :param point1y: y index of data
    :param point2x: x index of cluster
    :param point2y: y index of cluster
    :return: distance of cluster and data, xx.xxxxx
    """
    return round(((point1x - point2x) ** 2 + (point1y - point2y) ** 2) ** (1/2), 5)


# classify data with distance
def classify_data(point_num: int, cluster_num: int, point_list_x: list, point_list_y: list, cluster_list_x: list, cluster_list_y: list) -> list:
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
        # sum of x
        sum_point_x: int = sum([point_list_x[point_cluster_list[i][j]] for j in range(length_cluster)])
        # sum of y
        sum_point_y: int = sum([point_list_y[point_cluster_list[i][j]] for j in range(length_cluster)])

        # add replaced cluster
        cluster_list_x.append(round(sum_point_x / length_cluster))
        cluster_list_y.append(round(sum_point_y / length_cluster))

    return cluster_list_x, cluster_list_y


n: int = 500
limitx: int = 10000
limity: int = 10000
m: int = 5

x, y = make_random_points(n, limitx, limity)
X, Y = make_random_clusters(m, limitx, limity)
cluster_list: list = []

while True:
    X_pre = X[:]
    Y_pre = Y[:]
    classify_list: list = classify_data(n, m, x, y, X, Y)
    X, Y = replace_cluster(m, classify_list, x, y)
    if [X_pre, Y_pre] == [X, Y]:
        break


plt_guide: list = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i in range(m):
    # plt.plot(X[i], Y[i], f'{plt_guide[i]}o')
    plt.plot([x[j] for j in classify_list[i]], [y[j] for j in classify_list[i]], f'{plt_guide[i]}.')

plt.show()