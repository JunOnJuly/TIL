import random
import matplotlib.pyplot as plt
import math

def make_random_points(x_limit, data_num, theta_num):
    theta_list = [random.randint(-5, 5) for _ in range(theta_num)]

    data_x = random.choices(range(x_limit[0], x_limit[1]), k=data_num)
    data_y = cal_y_list_with_x_list(data_x, theta_list, theta_num)
    for i in range(data_num):
        data_y[i] += random.gauss(0, 50000)
    return data_x, data_y, theta_list


def cal_y_list_with_x_list(data_x, theta_list, theta_num):
    data_y = []

    for i in range(len(data_x)):
        x_list = [data_x[i]**j for j in range(theta_num)]

        data_y.append(sum([theta_list[j]*x_list[j] for j in range(theta_num)]))
    return data_y


def calculate_cost(data_x, data_y, theta_list, theta_num, data_num):
    cal_data_y = cal_y_list_with_x_list(data_x, theta_list, theta_num)
    h_x_list = [cal_data_y[i] - data_y[i] for i in range(data_num)]
    cost = sum([h_x_list[i]**2 for i in range(data_num)])/(2*data_num)
    return cost, h_x_list


def calculate_gradient(data_x, data_y, theta_list, theta_num, data_num):
    min_cost = math.inf
    recul_count = 0
    gradient_list = []

    while True:
        cost, h_x_list = calculate_cost(data_x, data_y, theta_list, theta_num, data_num)
        print(theta_list)
        print(f'cost = {cost}')

        if cost < min_cost:
            recul_count = 0
            min_cost = cost

            for i in range(theta_num):
                gradient = 0
                for j in range(data_num):
                    gradient += (data_x[j]**i) * h_x_list[j]
                gradient_list.append(gradient)
            alpha_list = []

            for i in range(theta_num):
                if gradient_list[i] > 0:
                    alpha_list.append(-round(math.log10(gradient_list[i]), 0)-1)
                elif gradient_list[i] == 0:
                    alpha_list.append(1)
                else:
                    alpha_list.append(-round(math.log10(-gradient_list[i]), 0)-1)
            print(f'alpha_list : {alpha_list}')
        else:
            if recul_count > 20:
                return theta_list
            else:
                recul_count += 1
                for i in range(theta_num):
                    alpha_list[i] -= 1

        for i in range(theta_num):
            theta_list[i] -= (10**alpha_list[i]) * gradient_list[i]



x_limit = [-100, 100]
data_num = 10
theta_num = 4
theta_list = [1 for _ in range(theta_num)]

data_x, data_y, origin_theta_list = make_random_points(x_limit, data_num, theta_num)

origin_x_list = [i/10 for i in range(x_limit[0]*10, x_limit[1]*10)]
origin_y_list = cal_y_list_with_x_list(origin_x_list, origin_theta_list, theta_num)

calculated_theta = calculate_gradient(data_x, data_y, theta_list, theta_num, data_num)

plt_title = ''
for i in range(theta_num):
    if i:
        if origin_theta_list[i] < 0:
            plt_title += f'-({-origin_theta_list[i]}x^{i})'
        elif origin_theta_list[i] == 0:
            continue
        else:
            plt_title += f'+({origin_theta_list[i]}x^{i})'
    else:
        plt_title += f'{origin_theta_list[i]}'

plt_title += '  |  '

calculated_y_list = cal_y_list_with_x_list(origin_x_list, calculated_theta, theta_num)

for i in range(theta_num):
    
    if i:
        if calculated_theta[i] < 0:
            plt_title += f'-({-round(calculated_theta[i], 4)}x^{i})'
        elif calculated_theta[i] == 0:
            continue
        else:
            plt_title += f'+({round(calculated_theta[i], 4)}x^{i})'
    else:
        plt_title += f'{round(calculated_theta[i], 4)}'

plt.plot(data_x, data_y, 'k.')
plt.plot(origin_x_list, origin_y_list, 'b')
plt.plot(origin_x_list, calculated_y_list, 'r')
plt.title(plt_title)
plt.show()