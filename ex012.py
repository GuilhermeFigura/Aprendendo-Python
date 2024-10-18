# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input(f'Qual é o preço do produto? R$ '))
preçonovo = preço * 0.95
print(f'O produto custa R$ {preço} e com desconto de 5% vai custar R$ {preçonovo:.2f}.')
