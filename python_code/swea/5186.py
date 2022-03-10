for tc in range(1, int(input()) + 1):
    N = float(input())

    print_num = ''
    tic = -1
    while True:
        if N == 0:
            print(f'#{tc} {(print_num)}')
            break
        elif len(print_num) >= 13:
            print(f'#{tc} overflow')
            break

        if N >= 2**tic:
            print_num = print_num + '1'
            N -= 2 ** tic
        else:
            print_num = print_num + '0'

        tic -= 1