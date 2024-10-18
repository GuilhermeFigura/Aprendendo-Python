""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. """
import time

salário = float(input(f'Digite o seu salário: R$ '))
print(f'Calculando o reajuste....')
time.sleep(5)

if salário <= 1250:
    print(f'Seu salário terá reajuste de 15%, novo valor é R$ {salário * 1.15:.2f}.')
else:
    print(f'Seu salário terá reajuste de 10%, novo valor é R$ {salário * 1.10:.2f}.')
