dict_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    find_code_list = []

    code_input = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(len(code_input)):
        for j in range(len(code_input[i]) - 1, -1, -1):
            if code_input[i][j] == 1:
                for k in range(j, j - 56, -7):
                    find_code_list.insert(0, ''.join(list(map(str, code_input[i][k - 6:k + 1]))))
                break
            else:
                continue
        if find_code_list:
            break
    for i in range(len(find_code_list)):
        find_code_list[i] = dict_code[find_code_list[i]]
    confirm_code = 0
    for i in range(len(find_code_list)):
        if not i % 2:
            confirm_code += find_code_list[i] * 3
        else:
            confirm_code += find_code_list[i]

    if not confirm_code % 10:
        print(f'#{tc} {sum(find_code_list)}')
    else:
        print(f'#{tc} {0}')