input_list = input("Введіть список цілих чисел, розділених пробілом: ")
list = list(map(int, input_list.split()))

k = int(input("Введіть k (позитивне - вправо, негативне - вліво): "))
n = len(list)

if n > 0:
    effective_shift = k % n
    if effective_shift != 0:
        split_point = n - effective_shift
        list = list[split_point:] + list[:split_point]

print(f"Зсув k: {k}")
print(f"Змінений список: {list}")