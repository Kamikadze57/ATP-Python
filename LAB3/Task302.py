# Надрукувати всі непарні числа з інтервалу [a, b] (a ≥ b). Розглянути
# варіант програми без використання інструкції розгалуження.

number = int(input("Введіть ціле число a (a ≥ b): "))
limit = int(input("Введіть ціле число b: "))
start_num = limit + (1 - (limit % 2))

print(f"Непарні числа в інтервалі [{limit}, {number}]:")
for num in range(start_num, number + 1, 2):
    print(num)