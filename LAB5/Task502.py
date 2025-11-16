n_input = input("Введіть ціле число n: ")
n_str = str(n_input) 

possible_numbers = []
length = len(n_str)

for i in range(length):
    # n_str[:i] - частина рядка до індексу i
    # n_str[i+1:] - частина рядка після індексу i
    new_str = n_str[:i] + n_str[i+1:]
    new_number = int(new_str)
    possible_numbers.append(new_number)
max_possible_number = max(possible_numbers)

print(f"Початкове число: {n_input}")
print(f"Найбільше після видалення цифри: {max_possible_number}")