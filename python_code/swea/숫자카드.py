T = int(input())

for i in range(T):
    N = int(input())
    card_list = list(map(int, list(input())))

    num_list = [0] * 10

    for j in range(len(card_list)):
        num_list[card_list[j]] += 1

    max_num = [0, 0]

    for j in range(len(num_list)):
        if max_num[1] <= num_list[j]:
            max_num = [j, num_list[j]]

    print(f'#{i+1}', end=' ')

    print(*max_num)