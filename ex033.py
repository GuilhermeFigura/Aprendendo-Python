""" Faça um programa que leia três números e mostre qual é o maior e qual é o menor. """
n1 = float(input(f'Digite o 1º número: '))
n2 = float(input(f'Digite o 2º número: '))
n3 = float(input(f'Digite o 3º número: '))
menor = n1

# verificando quem é menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O MENOR número é {menor}!')
print(f'O MAIOR número é {maior}!')
