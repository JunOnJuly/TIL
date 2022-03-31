def find_run_or_triplet(card_data):
    card_data = sorted(card_data)

    count_run = 0
    for i in range(len(card_data) - 1):
        if count_run == 2:
            return 1
        if card_data[i] == card_data[i + 1]:
            count_run += 1
            continue
        else:
            count_run = 0

        if card_data[i] == card_data[i + 1] - 1:
            if card_data[i + 1] + 1 in card_data:
                return 1


T = int(input())

for tc in range(1, T + 1):
    data_input = list(map(int, input().split()))

    player1 = []
    player2 = []

    for i in range(6):
        player1.append(data_input[2*i])

        if i >= 2:
            if find_run_or_triplet(player1):
                print(f'#{tc} {1}')
                break

        player2.append(data_input[2*i + 1])

        if i >= 2:
            if find_run_or_triplet(player2):
                print(f'#{tc} {2}')
                break

        if i == 5:
            print(f'#{tc} {0}')