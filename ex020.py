''''Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. O mesmo professor do desafio 19 quer
sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random
n1 = str(input(f'Digite o 1º aluno: '))
n2 = str(input(f'Digite o 2º aluno: '))
n3 = str(input(f'Digite o 3º aluno: '))
n4 = str(input(f'Digite o 4º aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem da apresentação será {lista}')
