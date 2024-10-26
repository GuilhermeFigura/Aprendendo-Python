"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

# Pega o primeiro peso
peso = float(input('Digite peso da 1º pessoa em KG: '))
máximo = peso
mínimo = peso

# Pega os outros 4 pesos
for pessoas in range(2, 6):
    peso = float(input(f'Digite peso da {pessoas}º pessoa em KG: '))
    if peso >= máximo:
        máximo = peso
    if peso <= mínimo:
        mínimo = peso
print(f'O peso máximo é {máximo}KG e o mínimo é {mínimo}KG.')
