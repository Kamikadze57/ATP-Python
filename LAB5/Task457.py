input = input("Введіть три цілих числа: ")
numbers = list(map(int, input.split()))

sorted_numbers = sorted(numbers)
median = sorted_numbers[1]

print(f"Введені числа: {numbers}")
print(f"Медіана: {median}")