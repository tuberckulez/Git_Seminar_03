# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

first = input('Введите первую дробь: ').split('/')
second = input('Введите первую дробь: ').split('/')

num_summ = int(first[0]) * int(second[1]) + int(second[0]) * int(first[1])
denom_summ = int(first[1]) * int(second[1])
summ_fract = [num_summ, denom_summ]

multi_fract = [int(first[0]) * int(second[0]), int(first[1]) * int(second[1])]

a1, b1 = summ_fract
while b1:
    a1, b1 = b1, a1 % b1
a2, b2 = multi_fract
while b2:
    a2, b2 = b2, a2 % b2


print(f'{summ_fract[0]//a1}/{summ_fract[1]//a1}', f'{multi_fract[0]//a2}/{multi_fract[1]//a2}')
first_f = Fraction(f'{first[0]}/{first[1]}')
second_f = Fraction(f'{second[0]}/{second[1]}')
print(first_f + second_f, first_f * second_f)
