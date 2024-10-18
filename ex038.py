""" Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem """
n1 = int(input(f'Digite o 1º número inteiro: '))
n2 = int(input(f'Digite o 2º número inteiro: '))

if n1 > n2:
    print(f'O 1º número é MAIOR!')
elif n2 > n1:
    print(f'O 2º número é MAIOR!')
else:
    print(f'Não existe valor MAIOR ou MENOR, são IGUAIS!')
