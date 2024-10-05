import array

M = int(input("Введіть число M: "))
N = int(input("Введіть кількість елементів N: "))

arr = array.array('i')

for i in range(1, N + 1):
    arr.append(M * i)

print("Масив чисел, кратних M:", arr)
