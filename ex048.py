""" Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500."""
quantidade = 0
soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        quantidade = quantidade + 1
        soma = soma + c
print(f'A soma dos {quantidade} valores solicitados é {soma}')

