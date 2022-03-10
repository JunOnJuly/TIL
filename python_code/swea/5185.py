def make_digit(num, return_num):
    if not num // 2:
        return_num = str(num % 2) + return_num
        while True:
            if len(return_num) >= 4:
                break
            else:
                return_num = '0' + return_num

        global digit_num
        digit_num = return_num

        return

    make_digit(num // 2, str(num % 2) + return_num)


dict_trans = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
for i in range(10):
    dict_trans[str(i)] = i

for tc in range(1, int(input()) + 1):
    N, num_input = map(list, input().split())
    digit_num = ''

    for i in range(len(num_input)):
        num_input[i] = dict_trans[num_input[i]]
        make_digit(num_input[i], '')
        num_input[i] = digit_num

    print(f"#{tc} {''.join(num_input)}")