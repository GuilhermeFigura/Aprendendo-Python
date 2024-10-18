"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
 com uma pausa de 1 segundo entre eles. """

import time
print('Os FOGOS DE ARTIFÍCIO irão começar em 10 segundos!!')

for c in range(10, 0, -1):
    print(f'Faltam {c} segundos')
    time.sleep(0.5) # Pausa por 1 segundo
print(f'BOOM  💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')

