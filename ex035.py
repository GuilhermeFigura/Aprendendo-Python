""" Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. """

reta1 = float(input(f'Digite o comprimento em CENTÍMETROS da 1º reta: '))
reta2 = float(input(f'Digite o comprimento em CENTÍMETROS da 2º reta: '))
reta3 = float(input(f'Digite o comprimento em CENTÍMETROS da 3º reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'É POSSÍVEL formar um triângulo com as retas informadas!')
else:
    print(f'NÃO É POSSÍVEL formar um triângulo com as retas informadas!')
