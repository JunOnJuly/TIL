M = int(input())
N = int(input())

list_prime = [2]

for i in range(2, N + 1):
    for j in range(len(list_prime)):
        if i % list_prime[j]:
            if j == len(list_prime) - 1:
                list_prime.append(i)
                break
        else:
            break

sum_prime = 0

switch = 0

for i in range(len(list_prime)):
    if M <= list_prime[i] <= N:
        if switch == 0:
            min_prime = list_prime[i]
            switch += 1
        sum_prime += list_prime[i]

if switch == 1:
    print(sum_prime)
    print(min_prime)
else:
    print(-1)