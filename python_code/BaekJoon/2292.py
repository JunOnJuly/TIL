N = int(input())

i = 0
while True:
    if N <= 3*(i**2) + 3*i + 1:
        print(i + 1)
        break
    i += 1