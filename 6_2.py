import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть крок h: "))

values = []

print("\nТабулювання функції з циклом з передумовою:")
x = a
while x <= b:
    value = x * math.sin(x) + math.exp(x)
    values.append(value)
    print(f"f({x:.2f}) = {value:.4f}")
    x += h

print("\nСписок значень функції:", values)
