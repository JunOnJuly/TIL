def find_path_to_end(rule_list):
    dict_path = {}
    for i in range(len(rule_list))[::-1]:
        if rule_list[i][1] in dict_path.keys():
            dict_path[rule_list[i][1]] += [rule_list[i][0]]
        else:
            dict_path[rule_list[i][1]] = [rule_list[i][0]]

    return dict_path


def change_path_to_time(dict_path, rule_time):
    dict_time = {}
    for key, value in dict_path.items():
        dict_time[key] = max([rule_time[x-1] for x in value])

    for i in range(len(rule_time)):
        if i + 1 not in dict_time.keys():
            dict_time[i+1] = rule_time[i]

    return dict_time


def path_maker(dict_path, dict_time, win_rule):
    min_time = 0
    while True:
        sum_time = 0
        if win_rule not in dict_path.keys():
            sum_time += dict_time[win_rule]
            if min_time == 0:
                min_time = sum_time

            elif sum_time < min_time:
                min_time = sum_time
            break
        sum_time += dict_time[win_rule]
        if len(dict_path[win_rule]) > 1:
            for i in range(len(dict_path[win_rule])):
                win_rule = dict_path[win_rule][0]
        else:
            win_rule = dict_path[win_rule][0]


T = int(input())

for i in range(T):
    N, K = map(int,input().split())

    D_list = list(map(int, input().split()))
    num_1 = D_list[0]
    K_list = []

    for _ in range(K):
        K_list.append(list(map(int, input().split())))

    W = int(input())

    dict_path = find_path_to_end(K_list)
    dict_time = change_path_to_time(dict_path, D_list)

    print(dict_path)
    print(dict_time)

