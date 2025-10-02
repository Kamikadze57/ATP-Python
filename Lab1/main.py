# Завдання 14
def sumNumbers(a,b):
    result = f"({a} + {b}) * ({a} + {b}) = {(a + b) * (a + b)}"
    print(result)
sumNumbers(8, 7)


# Завдання 39
def PrintDifferentTypes():
    inputInt = int(input("Введіть ціле число: "))
    inputString = str(input("Введіть рядок: "))
    inputFloat = float(input("Введіть дійсне число: "))
    return print(f"Ціле число: {inputInt} {type(inputInt)}, \
рядок: {inputString} {type(inputString)}, \
дійсне число: {inputFloat} {type(inputFloat)}")
PrintDifferentTypes()

# Завдання 9
def helloName():
    name = input("Введіть ваше ім'я: ")
    return print(f"Hello, {name}!")
helloName()

# Завдання 60
def calcSleepTime():
    timeToSleep = int(input("Скільки хвилин хочете спати: "))
    hours = timeToSleep // 60
    minutes = timeToSleep % 60
    return print(f"Ви хочете спати {hours} годин та {minutes} хвилин")
calcSleepTime()

# Завдання 69
def bigNumberToSquare():
    numberInp= int(input("Введіть ціле число: "))
    number = str(numberInp) * 100
    result = int(number) ** 2
    return print(f"Квадрат числа {numberInp}, записанного 100 раз = {result}")
bigNumberToSquare()

# Завдання 92
def lessonEndTime():
	lesson_number = int(input("Введіть номер уроку (1-10): "))
	minutes = 45 * lesson_number  # тривалість усіх уроків
	breaks = (lesson_number - 1)
	minutes += (breaks // 2) * 20 + (breaks % 2) * 5
	hour = 9 + minutes // 60
	minute = minutes % 60
	print(f"Урок закінчиться в: {hour}:{minute}")
lessonEndTime()
