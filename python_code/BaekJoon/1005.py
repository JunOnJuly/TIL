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
        dict_time[key] = max([rule_time[x] for x in value])

    return dict_time


def path_maker(dict_path, rule_win):
    path = []
    for i in range(len(dict_path)):
        if dict_path.keys()[i] == rule_win:



T = int(input())

for i in range(T):
    N, K = map(int,input().split())

    D_list = list(map(int, input().split()))
    K_list = []

    for _ in range(K):
        K_list.append(list(map(int, input().split())))

    W = int(input())

    print(find_path_to_end(K_list))
    print(change_path_to_time(find_path_to_end(K_list), D_list))
    print(path_maker(find_path_to_end(K_list), W))