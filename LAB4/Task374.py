# 374. Дано два слова. Складіть програму, що визначає чи можна чи ні з букв слова A скласти слово B.
# Програма має враховувати регістр літер введених слів.

frWord = input("Введіть слово A (джерело букв): ")
secWord = input("Введіть слово B (цільове слово): ")

count_a = {}
for letter in frWord:
    if letter in count_a:
        count_a[letter] += 1
    else:
        count_a[letter] = 1

count_b = {}
for letter in secWord:
    if letter in count_b:
        count_b[letter] += 1
    else:
        count_b[letter] = 1

can_be_composed = True

for letter, required_count in count_b.items():
    available_count = count_a.get(letter, 0)
    if available_count < required_count:
        can_be_composed = False
        break

if can_be_composed:
    print(f"Слово '{secWord}' можна скласти з букв слова '{frWord}'.")
else:
    print(f"Слово '{secWord}' не можна скласти з букв слова '{frWord}'.")