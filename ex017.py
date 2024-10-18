'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
 mostre o comprimento da hipotenusa. '''
import math
oposto = float(input(f'Digite o comprimento do cateto oposto: '))
adjacente = float(input(f'Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
