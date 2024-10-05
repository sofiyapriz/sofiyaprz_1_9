from collections import Counter

def max_repeated_char_string(strings):
    max_count = 0
    result_string = ""
    
    for s in strings:
        
        char_count = Counter(s)
        
        most_common_char, count = char_count.most_common(1)[0]
        
        if count > max_count:
            max_count = count
            result_string = s
            
    return result_string

N = int(input("Введіть кількість рядків: "))

strings = [input(f"Введіть рядок {i + 1}: ") for i in range(N)]

result = max_repeated_char_string(strings)

print("Рядок з найбільшою кількістю однакових символів:", result)
