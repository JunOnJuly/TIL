def mean(scores):
    sum_scores = sum(scores)
    return round(sum_scores/len(scores), 3)


C = int(input())

for _ in range(C):
    N, *scores = list(map(int, input().split()))
    avg = mean(scores)
    over_num = 0

    for i, score in enumerate(scores):
        if score > avg:
            over_num += 1

    print(f'{over_num/N*100:.3f}%')