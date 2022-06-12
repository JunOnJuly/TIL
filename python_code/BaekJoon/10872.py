def factor(N, mul):
    if N <= 1:
        return mul
    return factor(N - 1, mul * N)


N = int(input())
print(factor(N, 1))