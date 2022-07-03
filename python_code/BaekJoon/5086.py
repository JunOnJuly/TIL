while True:
    num_1, num_2 = map(int, input().split())

    if not num_1 and not num_2:
        break

    if num_1 > num_2 and not num_1 % num_2:
        print('multiple')

    elif num_1 < num_2 and not num_2 % num_1:
        print('factor')

    else:
        print('neither')