f = open('input.txt', 'r')
numbers = []
for num in f:
    numbers.append(int(num))

for i in range(len(numbers)):
    j = i + 1
    for k in range(j, len(numbers)):
        if numbers[i] + numbers[k] == 2020:
            print(numbers[i] * numbers[k])
            break

N = len(numbers)
for i in range(N - 1):
    for j in range(N - 1, i, -1):
        if numbers[j] > numbers[j - 1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

i = 0
j = len(numbers) - 1
while(True):
    if numbers[i] + numbers[j] == 2020:
        print(numbers[i] * numbers[j])
        break
    elif numbers[i] + numbers[j] > 2020:
        i += 1
    else:
        j -= 1
