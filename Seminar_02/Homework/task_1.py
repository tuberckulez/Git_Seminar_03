# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.
# import fractions

print("Задача 2 'Перевод из десятичной в систему исчисления с основанием от 2 до 16'")

number = int(input("введите целое число\n"))
base = int(input("введите основание системы счисления, в которую надо перевести число\n"))
num = abs(number)
number_new = ''

str_ = "0123456789abcdef"
while num:
    num_char = str_[num % base]
    number_new = num_char + number_new
    num //= base


if number < 0:
    number_new = "-" + number_new
if number == 0:
    number_new = "0"

print(f'Число {number} в {base}-ой системе счисления = {number_new}')
