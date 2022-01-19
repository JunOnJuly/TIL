# 연속된 배열을 얼마나 많이 찾아낼 수 있는가?
# 함수 정의
def factorial(number: int) -> int:
    if number == 0:
        return 1
    mul = 1
    for i in range(number):
        mul *= (i + 1)
    return mul


def find_neigh(xi_di: list, idx: int) -> list:
    neigh_list = []
    for i in range(len(xi_di[idx])):
        for j in range(i + 1, len(xi_di[idx])):
            if (xi_di[idx][i][0] == xi_di[idx][j][0] + 1) or (xi_di[idx][i][0] == xi_di[idx][j][0] - 1):
                if xi_di[idx][j][0] not in neigh_list:
                    neigh_list.append(xi_di[idx][j][0])

        if xi_di[idx][i][0] not in neigh_list:
            neigh_list.append(xi_di[idx][i][0])

    for i in range(len(neigh_list)):
        for j in range(len(xi_di[idx])):
            if neigh_list[i] == xi_di[idx][j][0]:
                xi_di[idx][j][1] -= 1

    while True:
        for i in range(len(xi_di[idx])):
            if xi_di[idx][i][1] == 0:
                del xi_di[idx][i]
                break

        num = 0

        for i in range(len(xi_di[idx])):
            if xi_di[idx][i][1] == 0:
                num += 1

        if num == 0:
            break

    return sorted(neigh_list), xi_di[idx]


# 변수 입력
num_test = int(input())

n = []
xi_di = []
for j in range(num_test):
    xi_di.append([])

for i in range(num_test):
    n.append(int(input()))

    for j in range(n[i]):
        xi_di[i].append(list(map(int, input().split())))


# 계산
final_num_neigh = []
for i in range(num_test):
    numbers_neigh = []
    split_neigh = []
    while True:
        neigh_list, xi_di_trans = find_neigh(xi_di, i)
        print(neigh_list)
        for j in range(len(neigh_list)-1):
            k = 0
            if neigh_list[j] + 1 == neigh_list[j + 1]:
                k += 1
                continue
            else:
                split_neigh.append(neigh_list[j-(k-1):j+1])
            print(f'neigh_list = {neigh_list}')
            split_neigh.append(neigh_list[len(neigh_list) - 1])
        for j in range(len(split_neigh)):
            print(f'split_neigh = {split_neigh}')
            numbers_neigh.append(len(split_neigh[j]))
        if len(neigh_list) == 0:
            break
    for j in range(len(numbers_neigh)):
        final_num_neigh.append(numbers_neigh[j])
    print(final_num_neigh)

for i in range(len(final_num_neigh)):
    mul = 1
    for j in range(len(final_num_neigh[i])):
        mul *= factorial(final_num_neigh[i][j])
    print(f'#{i} {mul}')
