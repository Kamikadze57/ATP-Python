fr_str = "6, 5, 8, 9, 11, 13, 1, 2, 6, 8"
sec_str = "5, 7, 9, 11, 13, 15, 17, 19, 5, 9"

fr_list = [int(x.strip()) for x in fr_str.split(',')]
sec_list = [int(x.strip()) for x in sec_str.split(',')]

fr_set = set(fr_list)
sec_set = set(sec_list)

common_elements_set = fr_set & sec_set

result_list = list(common_elements_set)

print(f"Числа 1: {fr_str}")
print(f"Числа 2: {sec_str}")
print(f"Спільні елементи: {result_list}")