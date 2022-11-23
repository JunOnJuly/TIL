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
        random_y = random.gauss(mu=random_x*degree, sigma=1000)

        point_list_x.append(random_x)
        point_list_y.append(random_y)
        point_list_xy.append([random_x, random_y])

    return point_list_x, point_list_y, point_list_xy


def calculate_cost(theta_list, random_data_x, random_data_y, num_data):
    simple_cost_list = []
    n = len(theta_list)
    cost = 0
    for i in range(num_data):
        y = 0
        for j in range(n):
            y += theta_list[j]*(random_data_x[i]**j)
            simple_cost_list.append(n/num_data)
        cost = cost + ((y - random_data_y[i])**2)
    return cost

num_data = 10
limit_x = 1000
alpha = 0.000005

theta_list = [0, 1, 1, 1]

random_data_x, random_data_y, random_data_xy = make_random_points(num_data, limit_x)

plt.plot(random_data_x, random_data_y, 'k.')

plt.show()