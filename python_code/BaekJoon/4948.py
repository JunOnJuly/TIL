from math import sqrt

while True:
    N = int(input())

    if not N:
        break

    list_print = [2]

    for num in range(3, 2*N + 1, 2):
        for i in range(len(list_print)):
            if not num % list_print[i]:
                break
            if i >= sqrt(num) + 1:
                list_print.append(num)
                break
            if i == len(list_print) - 1:
                list_print.append(num)
                break

    for i in range(len(list_print)):
        if list_print[i] > N:
            list_print = list_print[i:]
            break
    print(len(list_print))