# led

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    list_data = list(map(int, input().split()))

    tic = 0

    for i in range(1, N + 1):
        if list_data[i - 1] == 1:
            tic += 1
            for j in range(i, N + 1):
                if j % i == 0:
                    if list_data[j - 1]:
                        list_data[j - 1] = 0
                    else:
                        list_data[j - 1] = 1
                else:
                    continue
            print(list_data)
    print(f'#{tc} {tic}')
```

---

# 차르봄바

```python
T = int(input())

for tc in range(1, T + 1):
    n, p = map(int, input().split())

    list_input = []
    for i in range(n):
        list_input.append(list(map(int, input().split())))

    max_sum = 0
    for i in range(n):
        for j in range(n):
            sum_plus = 0
            sum_mul = 0

            idx = [i, j]

            for k in range(4):
                idx_i = [0, 1, 0, -1]
                idx_j = [1, 0, -1, 0]
                idx_i_mul = [1, 1, -1, -1]
                idx_j_mul = [1, -1, 1, -1]

                for l in range(p):
                    if idx[0] + (l+1) * idx_i[k] >= n or idx[0] + (l+1) * idx_i[k] < 0\
                            or idx[1] + (l+1) * idx_j[k] >= n or idx[1] + (l+1) * idx_j[k] < 0:
                        continue
                    else:
                        sum_plus += list_input[idx[0] + (l+1) * idx_i[k]][idx[1] + (l+1) * idx_j[k]]

                for l in range(p):
                    if idx[0] + (l+1) * idx_i_mul[k] >= n or idx[0] + (l+1) * idx_i_mul[k] < 0 \
                            or idx[1] + (l+1) * idx_j_mul[k] >= n or idx[1] + (l+1) * idx_j_mul[k] < 0:
                        continue
                    else:
                        sum_mul += list_input[idx[0] + (l+1) * idx_i_mul[k]][idx[1] + (l+1) * idx_j_mul[k]]

            sum_plus += list_input[idx[0]][idx[1]]
            sum_mul += list_input[idx[0]][idx[1]]

            if max_sum < sum_mul:
                max_sum = sum_mul
            if max_sum < sum_plus:
                max_sum = sum_plus
    print(f'#{tc} {max_sum}')
```