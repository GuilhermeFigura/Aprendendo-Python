'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input(f'Digite o seu nome completo: ')).strip().split()
print(nome)
print(f'Muito prazer em te conhecer!!')
print(f'O seu primeiro nome é {nome[0]} e o último nome é {nome[-1]}.')
