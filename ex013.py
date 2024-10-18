# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input(f'Qual o salário do funcionário? R$ '))
salárionovo = salário * 1.15
print(f'O salário atual de R$ {salário} com aumento de 15% ficará em R$ {salárionovo:.2f}')
