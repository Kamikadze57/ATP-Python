# 354.Напишіть програму для перевірки чи є введена літера голосною або приголосною.

letter = input("Введіть одну латинську літеру: ").lower()

if len(letter) != 1:
    print("Введено не одну літеру")
elif letter >= 'a' and letter <= 'z':
    if (letter == 'a' or letter == 'e' or letter == 'i' or 
        letter == 'o' or letter == 'u' or letter == 'y'):
        print("це голосна літера")
    else:
        print("це приголосна літера")
else:
    print("це не латинська літера")
