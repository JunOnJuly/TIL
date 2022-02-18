M, N = map(int, input().split())

list_print = [2] + list(range(3, N + 1, 2))

i = 0
while True:
    if i >= N // 2 + 1:
        break
    if i >= len(list_print) - 1:
        break
    num = list_print[i]
    j = i + 1
    while True:
        if j == len(list_print):
            break
        if not list_print[j] % list_print[i]:
            del list_print[j]
        else:
            j += 1
    i += 1

for num in list_print:
    if M <= num <= N:
        print(num)