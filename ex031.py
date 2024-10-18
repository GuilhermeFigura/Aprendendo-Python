""" Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200Km e R$0,45 parta viagens mais longas. """

km = float(input(f'Qual é a distância da  sua viagem em km? '))
print(f'Você está prestes a iniciar uma viagem de {km}km.')
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f'A sua passagem terá o custo de R$ {preço:.2f}')
