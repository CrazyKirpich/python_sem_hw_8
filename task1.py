# Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

grades = [int(i) for i in input('Введите оценки через пробел\n').split()]
# grades = [1, 2, 5, 5, 5, 3, 4, 1]
max = max(grades)
for i in range(len(grades)):
    if grades[i] == max:
        grades[i] = min(grades)
print(*grades)
