""" Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal."""

n = int(input(f'Digite um número inteiro: '))
print(f''' Escolha uma das bases de conversão:
    [1] Converter para BINÁRIO.
    [2] Converter para OCTAL.
    [3] Converter para HEXADECIMAL.''')
escolha = int(input(f'Opção: '))
if escolha == 1:
    binário = bin(n)[2:]
    print(f'O nº {n} convertido para BINÁRIO é igual {bin(n)[2:]}')
elif escolha == 2:
    octal = oct(n)[2:]
    print(f'O nª {n} convertido para BINÁRIO é igual {octal}')
elif escolha == 3:
    hexadecimal = hex(n)[2:]
    print(f'O nº {n} convertido para HEXADECIMAL é igual {hexadecimal}')
else:
    print(f'Opção INVÁLIDA tente novamente.')
