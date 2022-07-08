def split_by_alpha(string: str, alphabet: str) -> list:
    alpha_list.append(alphabet)
    return_list: list = []

    for idx in range(len(string)):
        if string[idx] == alphabet:
            return_list.append(idx)

    return return_list


alpha_list: list = []
S: str = input()
q: int = int(input())

for _ in range(q):
    data_input: list = input().split()

    alpha: str = data_input[0]
    l: int = data_input[1]
    r: int = data_input[2]

    if alpha not in alpha_list:
        alpha_index = split_by_alpha(S, alpha)

