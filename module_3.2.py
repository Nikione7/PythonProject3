# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(5)
print_params(False, 77, 'ice')
print_params(a=9, b=333)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = [1, 'winter', False]
values_dict = {'a': 2, 'b': "summer", 'c': 1.2}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [7, True]
print_params(*values_list_2, 42)
