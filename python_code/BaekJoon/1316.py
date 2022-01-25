num_test = int(input())

num_group = 0
for i in range(num_test):
    words = []
    word = input()
    for j in range(len(word)):
        if (word[j] in words) and (words[-1] != word[j]):
            break

        else:
            words.append(word[j])
            if j == len(word) - 1:
                num_group += 1

print(num_group)