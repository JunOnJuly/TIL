def split_by_alpha(string: str, alphabet: str) -> list:
    alpha_list[alphabet] = []
    return_list: list = []

    for idx in range(len(string)):
        if string[idx] == alphabet:
            alpha_list[alphabet].append(idx)
            return_list.append(idx)

    return return_list


alpha_list: dict = {}
S: str = input()
q: int = int(input())

for _ in range(q):
    data_input: list = input().split()

    alpha: str = data_input[0]
    l: int = int(data_input[1])
    r: int = int(data_input[2])

    if alpha not in alpha_list.keys():
        alpha_index: list = split_by_alpha(S, alpha)
    else:
        alpha_index: list = alpha_list[alpha]

    for idx_start in range(len(alpha_list[alpha])):
        print(alpha_list[alpha])
        if l <= alpha_list[alpha][idx_start]:
            start: int = idx_start
            end: int = 0

            for idx_end in range(len(alpha_list[alpha])):
                if r >= alpha_list[alpha][idx_end]:
                    end: int = idx_end
                print(f'start:{start}\nend:{end}')
                print(len(alpha_list[alpha]) - (start - 1) + (end + 1))
                break
            break

        print(0)
