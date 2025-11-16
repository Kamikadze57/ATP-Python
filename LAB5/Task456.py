input_string = "0110,0111,1110,1011,1111"
divisible = []
binary_list = input_string.split(',')

for binary_num in binary_list:
    decimal_num = int(binary_num, 2)
    if decimal_num % 5 == 0:
        divisible.append(binary_num)
result_string = ",".join(divisible)

print(f"Відібрані двійкові числа (діляться на 5): {result_string}")