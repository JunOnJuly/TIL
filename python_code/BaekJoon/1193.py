X = int(input())

i = 1
while True:
    if X <= i*(i+1)/2:
        if i % 2 == 0:
            print(f'{int(X - (i*(i-1)/2))}/{int(i + 1 - (X - (i*(i-1)/2)))}')
            break
        else:
            print(f'{int(i + 1 - (X - (i * (i - 1) / 2)))}/{int(X - (i * (i - 1) / 2))}')
            break
    i += 1