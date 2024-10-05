import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть крок h: "))

values = []

print("\nТабулювання функції з циклом з параметром:")
for x in range(int(a * 100), int(b * 100) + 1, int(h * 100)):
    x = x / 100.0  # Перетворюємо назад до звичайного числа
    value = x * math.sin(x) + math.exp(x)
    values.append(value)
    print(f"f({x:.2f}) = {value:.4f}")

print("\nСписок значень функції:", values)
