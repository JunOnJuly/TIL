from math import sqrt

M, N = map(int, input().split())

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

for num in list_print:
    if num >= M:
        print(num)