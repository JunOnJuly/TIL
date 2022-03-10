def find_code(code_line):
    end_code_idx = 0
    list_return = []

    range_code = len(code_line) - 1
    for i in range(range_code, -1, -1):
        if code_line[i] != '0':
            if not end_code_idx:
                end_code_idx = i
        else:
            if end_code_idx:
                list_return.append(code_line[i:end_code_idx + 1])
                end_code_idx = 0
            continue

    return list_return


def change_0x(num_str):
    temp_list = []
    for i in range(len(num_str)):
        temp_list.append(int('0' + num_str[i].lower(), 16))
    for i in range(len(temp_list)):
        temp_list[i] = bin(temp_list[i])[2:].rjust(4, '0')
    return ''.join(temp_list)


def cut_code(code_line):
    return_list = []

    range_code = len(code_line) - 1
    for i in range(range_code, -1, -1):
        if code_line[i] == '1':
            for j in range(i, i-56, -7):
                return_list.append(code_line[j - 6:j + 1])
            break
    return_list.reverse()

    return return_list


def zip_code(code_line):
    range_code = len(code_line) - 1
    return_code = ''
    print(code_line, len(code_line))
    for i in range(range_code, -1, -1):
        if code_line[i] == '1':
            code_line = code_line[:i + 1]
            break

    zip_num = len(code_line) // 56
    if zip_num == 0:
        return None

    range_code = len(code_line) - 1
    for i in range(range_code, -1, -1):
        if not i % zip_num:
            return_code = code_line[i] + return_code
    return return_code


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

    codes_input = [input().strip() for _ in range(N)]
    codes_find = []
    for i in range(len(codes_input)):
        code_find = find_code(codes_input[i])
        if code_find:
            for j in range(len(code_find)):
                if code_find[j] not in codes_find:
                    codes_find.append(code_find[j])

    for i in range(len(codes_find)):
        codes_find[i] = change_0x(codes_find[i])
        if zip_code(codes_find[i]):
            codes_find[i] = zip_code(codes_find[i])
        else:
            continue
        codes_find[i] = cut_code(codes_find[i])
        for j in range(len(codes_find[i])):
            codes_find[i][j] = dict_code[codes_find[i][j]]
    print(codes_find)
    for i in range(len(codes_find)-1, -1, -1):
        if type(codes_find[i]) == str:
            del codes_find[i]

    sum_confirmed_code = 0
    for i in range(len(codes_find)):
        confirm_code = 0
        for j in range(len(codes_find[i])):
            if not j % 2:
                confirm_code += codes_find[i][j] * 3
            else:
                confirm_code += codes_find[i][j]
        if not confirm_code % 10:
            print(f'{tc} {confirm_code}')
            sum_confirmed_code += sum(codes_find[i])

    print(f'#{tc} {sum_confirmed_code}')