from math import sqrt

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    list_print = [2]

    for num in range(3, N + 1, 2):
        for i in range(len(list_print)):
            if not num % list_print[i]:
                break
            if i >= sqrt(num) + 1:
                list_print.append(num)
                break
            if i == len(list_print) - 1:
                list_print.append(num)
                break

    for i in range(0, len(list_print)):
        if list_print[i] >= N//2 + 1:
            break
        if N - list_print[i] in list_print:
            gold = [list_print[i], N - list_print[i]]
            continue

    print(gold[0], gold[1])