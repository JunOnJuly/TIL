N = int(input())

list_prime = [2]

num_prime = 0

list_input = list(map(int, input().split()))

for i in range(N):
    for j in range(2, list_input[i] + 1):
        if list_prime[-1] >= j:
            continue
        else:
            for k in range(len(list_prime)):
                if j % list_prime[k] != 0:
                    if k == len(list_prime) - 1:
                        list_prime.append(j)
                        break
                    continue

                else:
                    break

    if list_input[i] in list_prime:
        num_prime += 1

print(num_prime)