""" Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. """

print(f'*** Esse programa vai verificar se o número é PAR ou ÍMPAR ***')
número = int(input(f'Digite um número: '))
if número % 2 == 0:
    print(f'O número digitado é PAR.')
else:
    print(f'O número digitado é ÍMPAR')
