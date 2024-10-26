"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

import datetime

maioridade = 0
menoridade = 0
for c in range(0, 7):
    year = int(input('Digite o ano de nascimento: '))
    data = datetime.date.today().year - year
    if data >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print(f'Existem {maioridade} de pessoas com idade MAIOR de 18 anos e {menoridade} pessoas com idade MENOR de 18 anos')
