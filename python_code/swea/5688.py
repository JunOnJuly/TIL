T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    list_num = []
    print_num = 1
    i = 2
    cnt_i = 0
    switch = 0
    while True:
        if N % i == 0:
            list_num.append(i)
            N = N // i
            cnt_i += 1
        else:
            if cnt_i % 3:
                switch = 1
                break
            else:
                for _ in range(cnt_i // 3):
                    print_num *= i
                cnt_i = 0
                i += 1

            if N == 1:
                break

    if switch == 1:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {print_num}')