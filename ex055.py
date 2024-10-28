"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

máximo = 0
mínimo = 0
for pessoas in range(1, 6):
    peso = float(input(f'Digite peso da {pessoas}º pessoa em KG: '))
    if pessoas == 1:
        máximo = peso
        mínimo = peso
    else:
        if peso > máximo:
            máximo = peso
        if peso < mínimo:
            mínimo = peso
print(f'O peso máximo é {máximo}KG e o mínimo é {mínimo}KG.')
