# Завдання 115
def MaxNumber():
    frNum = int(input("Введіть перше число: "))
    secNum = int(input("Введіть друге число: "))
    if (frNum >= 1000 or frNum < 1) or (secNum >= 1000 or secNum < 1):
        print("Числа мають бути в діапазоні від 1 до 999.")
        return
    elif frNum > secNum:
        print(f"Найбільше число: {frNum}")
    elif secNum > frNum:
        print (f"Найбільше число: {secNum}")
    else:
        print ("Числа однакові")
MaxNumber()

# Завдання 140
def ifDivider():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    if (a % b == 0):
        print(f"{a} є дільником {b}")
    elif (b % a ==0):
        print(f"{b} є дільниокм {a}")
    else:
        print("Числа не є дільниками")
ifDivider()

# Завдання 165
def Calculator():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Введіть арифметичну дію (+, -, /, *, mod, pow, div): ")
    result = None
    if operation in ('/', 'mod', 'div') and num2 == 0:
        print("Division by 0!")
    # Основні операції
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    # Додаткові операції
    elif operation == 'mod':
        result = num1 % num2
    elif operation == 'pow':
        result = num1 ** num2
    elif operation == 'div':
        result = num1 // num2
    else:
        print("Непідтримувана арифметична дія")
    if result is not None:
        print(result)
Calculator()

# Завдання 170
def DigitRepeat():
    number = int(input("Введіть трицифрове ціле число: "))
    if not (100 <= number <= 999):
        print("Помилка: Введене число не є трицифровим.")
        return
    # сотні: цілочисельне ділення на 100
    digit1 = number // 100
    # десятки: залишок від ділення на 100, а потім цілочисельне ділення на 10
    digit2 = (number % 100) // 10
    # одиниці: залишок від ділення на 10
    digit3 = number % 10

    count = 0
    if digit1 == digit2 and digit2 == digit3:
        count = 3
    elif digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
        count = 2
    else:
        count = 0 
    print(f"Кількість однакових цифр у числі {number}: {count}")
DigitRepeat()

# Завдання 184
def BreakChokolate():
    n = int(input("Введіть кількість рядків (n): "))
    m = int(input("Введіть кількість стовпців (m): "))
    k = int(input("Введіть бажану кількість частин (k): "))
    total_parts = n * m

    is_possible = (k % n == 0 and k // n < m) or (k % m == 0 and k // m < n)

    if k == total_parts:
        print("No")
    elif k > total_parts:
        print("No")
    elif is_possible:
        print("Yes")
    else:
        print("No")
BreakChokolate()

# Завдання 193
def ChessTowerMove():
    # x1, y1 - стовпець і рядок першої клітинки
    #x2, y2 - стовпець і рядок другої клітинки
    x1 = int(input("Введіть стовпець першої клітинки (1-8): "))
    y1 = int(input("Введіть рядок першої клітинки (1-8): "))
    x2 = int(input("Введіть стовпець другої клітинки (1-8): "))
    y2 = int(input("Введіть рядок другої клітинки (1-8): "))
    # перевірка на коректність координат
    if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
        print("No")
        return
    # Тура може потрапити з (x1, y1) на (x2, y2) за один хід,
    # якщо стовпці однакові (вертикальний хід) АБО рядки однакові (горизонтальний хід)
    if x1 == x2 or y1 == y2:
        print("Yes")
    else:
        print("No")
ChessTowerMove()