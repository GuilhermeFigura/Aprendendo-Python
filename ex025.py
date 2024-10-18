'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = str(input(f'Digite o seu nome: ')).strip()
print(f'O seu nome tem Silva? {'SILVA' in nome.upper()}')
