N = int(input())

switch = 0
str_N = str(N)

if N <= len(str_N)*9:
    range_num = 0
else:
    range_num = N - len(str_N)*9

for num in range(range_num, N + 1):
    if switch == 1:
        break
    sum_num = num + 0
    str_num = str(num)

    for i in range(len(str_num)):
        if sum_num > N:
            break
        sum_num += int(str_num[i])

    if sum_num == N:
        print(num)
        switch = 1
        break
    elif num == N:
        print(0)