import random
import matplotlib.pyplot as plt
import math


def make_random_data(data_num, x_limit, factor_num, factor_limit):
    factors = random.choices(range(factor_limit[0], factor_limit[1]), k=factor_num)
    x_list = random.choices(range(x_limit[0], x_limit[1]), k=data_num)
    y_list = []

    for i in range(len(x_list)):
        real_y = 0
        for j in range(len(factors)):
            real_y += (x_list[i] ** j) * factors[j]
        y_list.append(real_y)

    print(x_list, y_list)
    return factors, x_list, y_list


def calculate_cost():
    pass


data_num = 10
x_limit = [-100, 100]
factor_num = 4
factor_limit = [-10, 10]

factors, x_list, y_list = make_random_data(data_num, x_limit, factor_num, factor_limit)

plot_x = [i/10 for i in range(10*x_limit[0], 10*x_limit[1])]
plot_y = []


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
        alpha = 10**-18
        for i in range(n):
            theta_list_cal[i] = theta_list[i] - (alpha*theta_list_cal[i])

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
limit_y = 100000000
alpha = 1

theta_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random_data_x, random_data_y, random_data_xy = make_random_points(num_data, limit_x, limit_y)
theta_list = calculate_gradient(theta_list, random_data_x, random_data_y, num_data, alpha)

plot_input_x = [i*0.01 for i in range(-limit_x*100, limit_x*101)]
plot_input_y = []

for i in range(len(plot_input_x)):
    y_cal = 0
    for j in range(len(theta_list)):
        y_cal += (plot_input_x[i]**j)*theta_list[j]
    plot_input_y.append(y_cal)

plt.plot(random_data_x, random_data_y, 'k.')
plt.plot(plot_input_x, plot_input_y, 'r')

print(plot_input_x, plot_input_y)
# plt.ylim([-limit_y, limit_y])

plt.plot(plot_x, plot_y, 'r')
plt.show()