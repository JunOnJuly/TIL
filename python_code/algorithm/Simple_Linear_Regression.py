import random
import matplotlib.pyplot as plt
import math

def make_random_points(num_data, limit_x):
    degree_trigger = random.randint(0, 2)

    if degree_trigger:
        degree = random.uniform(3, 5)
    else:
        degree = random.uniform(-5, -3)
    print(degree)
    point_list_x = []
    point_list_y = []
    point_list_xy = []

    for i in range(num_data):
        random_x = random.randint(-limit_x, limit_x+1)
        random_y = random.uniform((random_x - 0.5*limit_x) * degree, (random_x + 0.5*limit_x) * degree)

        point_list_x.append(random_x)
        point_list_y.append(random_y)
        point_list_xy.append([random_x, random_y])

    return point_list_x, point_list_y, point_list_xy


def simple_degree(point1_x, point1_y, point2_x, point2_y):
    degree = (point2_y - point1_y)/(point2_x - point1_x)
    x_intercept = point1_x - (point1_y/degree)
    y_intercept = -degree*point1_x + point1_y
    return (point2_y - point1_y)/(point2_x - point1_x),  x_intercept, y_intercept


def decide_degree(simple_degree, y_intercept, x_list, y_list, alpha):
    sum_value_min = 0
    sum_value_pl = 0

    for i in range(len(x_list)):
        sum_value_min += (y_list[i] - (x_list[i] * (simple_degree - alpha) + y_intercept)) ** 2

    for i in range(len(x_list)):
        sum_value_pl += (y_list[i] - (x_list[i] * (simple_degree + alpha) + y_intercept)) ** 2

    if sum_value_min > sum_value_pl:
        return simple_degree + alpha, sum_value_pl
    else:
        return simple_degree - alpha, sum_value_min


def linear_regression(simple_degree, y_intercept,  x_list, y_list, aplha):
    min_value = math.inf
    degree = simple_degree
    while True:
        print(degree)
        degree, value = decide_degree(degree, y_intercept, x_list, y_list, alpha)

        if min_value > value:
            min_value = value
            degree = degree
            continue
        else:
            return degree


num_data = 100
limit_x = 1000
alpha = 0.01

random_data_x, random_data_y, random_data_xy = make_random_points(num_data, limit_x)

temp_num_1 = random.randint(0, num_data+1)
while True:
    temp_num_2 = random.randint(0, num_data+1)
    if temp_num_1 == temp_num_2:
        continue
    break

temp_degree, x_intercept, y_intercept = simple_degree(random_data_x[temp_num_1], random_data_y[temp_num_1], random_data_x[temp_num_2], random_data_y[temp_num_2])

degree = linear_regression(temp_degree, y_intercept, random_data_x, random_data_y, alpha)
print(degree)
y_first = -limit_x*degree + y_intercept
y_last = limit_x*degree + y_intercept

plt.plot(random_data_x, random_data_y, 'k.')
plt.plot([-limit_x, limit_x], [y_first, y_last], 'k')

plt.show()