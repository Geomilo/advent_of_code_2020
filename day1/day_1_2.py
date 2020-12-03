f = open('input.txt', 'r')
numbers = []
for num in f:
    numbers.append(int(num))

for i in range(len(numbers)):
    j = i + 1
    for k in range(j, len(numbers)):
        l = j + 1
        for n in range(l, len(numbers)):
            if numbers[i] + numbers[k] + numbers[n] == 2020:
                print(numbers[i] * numbers[k] * numbers[n])
                break

N = len(numbers)
for i in range(N - 1):
    for j in range(N - 1, i, -1):
        if numbers[j] > numbers[j - 1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

for v in range(len(numbers)):
    new_num = numbers[v]
    i = v + 1
    j = len(numbers) - 1
    while(i < j):
        if numbers[i] + numbers[j] + new_num == 2020:
            print(numbers[i] * numbers[j] * new_num)
            break
        elif numbers[i] + numbers[j] + new_num > 2020:
            i += 1
        else:
            j -= 1
