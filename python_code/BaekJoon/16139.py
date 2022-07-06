def split_by_alpha(string: str, alpha: str) -> list:
    alpha_list.append(alpha)
    return_list: list = []

    for idx in range(len(string)):
        if string[idx] == alpha:
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
