N = int(input().strip())

for _ in range(N):
    A = list(map(int, input().split()))
    A = [A[0]] + sorted(A[1:], reverse=True)

    B = list(map(int, input().split()))
    B = [B[0]] + sorted(B[1:], reverse=True)

    i = 0
    while True:
        if (i == A[0]) or (i == B[0]):
            if A[0] > B[0]:
                print('A')
            elif A[0] < B[0]:
                print('B')
            else:
                print('D')
            break
        else:
            if A[1:][i] > B[1:][i]:
                print('A')
                i += 1
                break
            elif A[1:][i] < B[1:][i]:
                print('B')
                i += 1
                break
            else:
                i += 1
                continue