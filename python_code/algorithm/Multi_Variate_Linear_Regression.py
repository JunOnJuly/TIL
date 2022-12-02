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

for i in range(len(plot_x)):
    real_y = 0
    for j in range(len(factors)):
        real_y += (plot_x[i]**j) * factors[j]
    plot_y.append(real_y)

plt.plot(plot_x, plot_y, 'r')
plt.show()