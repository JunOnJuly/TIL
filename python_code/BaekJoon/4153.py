while True:
    input_list = sorted(list(map(int, input().split())))
    if input_list == [0, 0, 0]:
        break
    if input_list[0] ** 2 + input_list[1] ** 2 == input_list[2] ** 2:
        print('right')
    else:
        print('wrong')