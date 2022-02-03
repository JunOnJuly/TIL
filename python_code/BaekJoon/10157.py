C, R = map(int, input().split())
c, r = C + 0, R + 0

skin = (C + R - 2) * 2
num_cost = int(input().strip())

skin_in = 0

if num_cost > (C * R):
    print(0)
else:
    i = 0
    while True:
        if num_cost <= skin:
            skin_in = i + 0
            break
        else:
            num_cost = num_cost - skin
            skin = skin - 8
            i += 1
            c = c - 2
            r = r - 2

    if num_cost <= r - 1:
        print(f'{skin_in + 1} {skin_in + num_cost}')
    elif num_cost <= r + c - 1:
        print(f'{skin_in + 1 + num_cost - r} {skin_in + r}')
    elif num_cost <= 2*r + c - 2:
        print(f'{skin_in + c} {skin_in - 1 + r - (num_cost - r - c)}')
    else:
        print(f'{skin_in - 2 + c - (num_cost - 2*r - c)} {skin_in + 1}')
