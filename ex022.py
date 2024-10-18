'''Crie um programa que leia o nome completo de uma pessoa e mostre: 1) O nome com todas as letras maiúsculas e minúsculas.
2) Quantas letras ao todo (sem considerar espaços)
3)Quantas letras tem o primeiro nome.'''

nome = str(input(f'Digite o seu nome completo: ')).strip()
separa = nome.split()

print(f'O nome digitado em Maiúsculas é: {nome.upper()}.')
print(f'O nome digitado em Minúsculas é: {nome.lower()}.')
print(f'O nome digitado ao todo tem {len(nome) - nome.count(' ')} letras.')
print(f'O primeiro nome digitado possui {nome.find(' ')} letras.')
print(f'O primeiro nome digitado é {separa[0]} e possui {len(separa[0])} letras.')
