import random
import matplotlib.pyplot as plt
import math


def make_random_points(num_data, limit_x, limit_y):
    point_list_x = [-5, -3, -1, 1, 3, 5]
    point_list_y = [random.randint(-limit_y, limit_y + 1) for _ in range(num_data)]
    point_list_xy = []
    for i in range(num_data):
        point_list_xy.append([point_list_x[i], point_list_y[i]])


    return point_list_x, point_list_y, point_list_xy


def calculate_cost(theta_list, random_data_x, random_data_y, num_data):
    gradient_cost = []
    cost = 0
    n = len(theta_list)
    for i in range(num_data):
        sum_function = 0
        for j in range(n):
            sum_function += theta_list[j] * (random_data_x[i]**j)
        cost += (sum_function - random_data_y[i]) ** 2

        for j in range(n):
            gradient_cost.append((sum_function - random_data_y[i]) * (random_data_x[i]**j) / num_data)

    cost = cost / (2*num_data)

    return cost, gradient_cost


def calculate_gradient(theta_list, random_data_x, random_data_y, num_data, alpha):
    min_cost = math.inf
    min_count = 0
    theta_list = theta_list
    n = len(theta_list)

    while True:
        print(min_count)
        for i in range(n):
            if i:
                print(f' + {theta_list[i]}x^{i}', end='')
                if i == n-1:
                    print('')
            else:
                print(f'h(x) = {theta_list[i]}', end='')

        cost, theta_list_cal = calculate_cost(theta_list, random_data_x, random_data_y, num_data)
        print(cost)
        alpha = 10**-9
        for i in range(n):
            theta_list_cal[i] = round(theta_list[i] - (alpha*theta_list_cal[i]), 4)

        if min_cost > cost:
            min_cost = cost
            min_count = 0
            for i in range(n):
                theta_list[i] = theta_list_cal[i]

        else:
            if min_count == 10:
                break
            min_count += 1

    return theta_list

num_data = 6
limit_x = 5
limit_y = 1000
alpha = 1

theta_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random_data_x, random_data_y, random_data_xy = make_random_points(num_data, limit_x, limit_y)
theta_list = calculate_gradient(theta_list, random_data_x, random_data_y, num_data, alpha)

plot_input_x = [i*0.01 for i in range(-limit_x*100, limit_x+1*100)]
plot_input_y = []

for i in range(len(plot_input_x)):
    y_cal = 0
    for j in range(len(theta_list)):
        y_cal += (plot_input_x[i]**j)*theta_list[j]
    plot_input_y.append(y_cal)

plt.plot(random_data_x, random_data_y, 'k.')
plt.plot(plot_input_x, plot_input_y, 'r')

print(plot_input_x, plot_input_y)
plt.ylim([-limit_y, limit_y])

plt.show()