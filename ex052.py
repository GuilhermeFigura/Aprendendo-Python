"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

primo = int(input(f'Digite um número: '))
total = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print(f'\033[33m {c}', end='')
        total = total + 1
    else:
        print(f'\033[31m {c}', end='')
print(f'\n\033[m0 número {primo} foi divisível {total} vezes.')
if total == 2:
    print(f'O número é PRIMO.')
else:
    print(f'O número NÃO é PRIMO.')
50