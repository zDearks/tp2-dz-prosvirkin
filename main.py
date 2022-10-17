from functions import _min, _max, _sum, _mult

with open(input('Файл:')) as file:
        array = list(map(int, file.readline().split()))

print('Минимум', _min(array))
print('Максимум', _max(array))
print('Сумма', _sum(array))
print('Произведение', _mult(array))


