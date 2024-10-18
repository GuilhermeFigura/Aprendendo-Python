'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

n = int(input(f'Digite um número entre 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número {n}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

"""
n1 = str(n)
print(f'Analisando o número {n}')
print(f'Unidade: {n1[3]}')
print(f'Dezena: {n1[2]}')
print(f'Centena: {n1[1]}')
print(f'Milhar: {n1[0]}') 
"""