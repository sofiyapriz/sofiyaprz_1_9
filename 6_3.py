import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть крок h: "))

values = []

x = a
while x <= b:
    value = x * math.sin(x) + math.exp(x)
    values.append(value)
    x += h

print("\nСписок значень функції:", values)

sorted_values = sorted(values)

print("Відсортований список значень функції:", sorted_values)
