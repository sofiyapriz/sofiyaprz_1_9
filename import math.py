import math

# Функція для обчислення значення f(x)
def f(x):
    try:
        # Обчислюємо основні частини функції
        sin_x = math.sin(x)
        log_base_10 = math.log10(abs(x - x**4))
        log_base_4 = math.log10(x) / math.log10(4)
        
        # Обчислюємо значення функції
        result = (x + sin_x) / log_base_10 * log_base_4
        return result
    except ValueError as e:
        return f"Помилка: {e}"
    except ZeroDivisionError:
        return "Помилка: ділення на нуль."

# Зчитуємо значення x з консолі
x = float(input("Введіть значення x: "))

# Виводимо результат обчислення функції
result = f(x)
print(f"Значення f(x): {result}")