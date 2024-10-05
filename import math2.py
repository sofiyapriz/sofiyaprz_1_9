import math

# Функція для обчислення значення F
def F(x, a, b):
    try:
        # Обчислюємо основні частини функції
        tan_x = math.tan(x)
        exp_part = math.exp(a - b)
        log_base_4_part = math.log10(abs(x**2 + 0.7)) / math.log10(4)
        
        # Обчислюємо значення F
        result = x * tan_x * exp_part + log_base_4_part
        return result
    except ValueError as e:
        return f"Помилка: {e}"
    except ZeroDivisionError:
        return "Помилка: ділення на нуль."

# Зчитуємо значення x, a і b з консолі
x = float(input("Введіть значення x: "))
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

# Виводимо результат обчислення функції
result = F(x, a, b)
print(f"Значення F: {result}")