""" Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
 ele foi multado. A multa vai custar R$7,00 por cada km acima do limite. """

velocidade = float(input(f'Qual a velocidade atual do carro em km/h? '))
multa = 7
if velocidade > 80:
    print(f'Você foi multado no valor de R$ {(velocidade - 80) * 7} por ultrapassar 80km/h.')
else:
    print(f'Você estava á {velocidade} km/h.')
