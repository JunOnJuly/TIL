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


def calculate_cost(theta_0, theta_1, random_data_x, random_data_y, num_data):
    simple_cost_0 = 0
    simple_cost_1 = 0
    cost = 0
    for i in range(num_data):
        simple_cost_0 += theta_0 + random_data_x[i]*theta_1 - random_data_y[i]
        simple_cost_1 += (theta_0 + random_data_x[i]*theta_1 - random_data_y[i])*random_data_x[i]
        cost += (theta_0 + random_data_x[i]*theta_1 - random_data_y[i]) ** 2

    return round(cost / (2*num_data), 4), round(simple_cost_0/num_data, 4), round(simple_cost_1/num_data, 4)


def calculate_gradient(theta_0, theta_1, random_data_x, random_data_y, num_data, alpha):
    min_cost = math.inf
    min_count = 0
    min_theta_0 = 0
    min_theta_1 = 1

    while True:
        cost, simple_cost_0, simple_cost_1 = calculate_cost(theta_0, theta_1, random_data_x, random_data_y, num_data)

        theta_0 = round(theta_0 - (alpha*(simple_cost_0)), 4)
        theta_1 = round(theta_1 - (alpha*(simple_cost_1)), 4)

        if min_cost > cost:
            min_cost = cost
            min_count = 0
            min_theta_0 = theta_0
            min_theta_1 = theta_1

        else:
            if min_count == 10:
                break
            min_count += 1

    return min_theta_0, min_theta_1


num_data = 200
limit_x = 1000
alpha = 0.000005

theta_0 = 0
theta_1 = 1

random_data_x, random_data_y, random_data_xy = make_random_points(num_data, limit_x)
cost = calculate_cost(theta_0, theta_1, random_data_x, random_data_y, num_data)
theta_0, theta_1 = calculate_gradient(theta_0, theta_1, random_data_x, random_data_y, num_data, alpha)

print(f'h(x) = {theta_0} + {theta_1}x')

plt.plot(random_data_x, random_data_y, 'k.')
plt.plot([-limit_x, limit_x], [-limit_x*theta_1 + theta_0, limit_x*theta_1 + theta_0], 'r')

plt.show()