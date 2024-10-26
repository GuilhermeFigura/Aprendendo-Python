"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

import datetime

data = datetime.date.today().year
maioridade = 0
menoridade = 0
for pessoas in range(1, 8):
    nascimento = int(input(f'Em quem ano a {pessoas}ª pessoa nasceu? '))
    idade = data - nascimento
    if idade >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print(f'Existem {maioridade} de pessoas com idade MAIOR de 18 anos.'
      f'\nE existem {menoridade} pessoas com idade MENOR de 18 anos.')
