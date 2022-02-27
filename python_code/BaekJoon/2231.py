N = int(input())

switch = 0

if len(str(N)) == 1:
    print(0)

else:
    if N > len(str(N))*9:
        for num in range(N-len(str(N))*9, N + 1):
            if switch == 1:
                break
            str_num = str(num)
            num_sum = num + 0

            for i in range(len(str_num)):
                num_sum += int(str_num[i])

            if num_sum == N:
                print(num)
                switch = 1
                break

            elif num == N:
                print(0)
    else:
        for num in range(0, N + 1):
            if switch == 1:
                break
            str_num = str(num)
            num_sum = num + 0

            for i in range(len(str_num)):
                num_sum += int(str_num[i])

            if num_sum == N:
                print(num)
                switch = 1
                break

            elif num == N:
                print(0)