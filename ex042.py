"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes"""

side1 = int(input(f'Digite o comprimento em CENTÍMETROS da 1º reta do triângulo: '))
side2 = int(input(f'Digite o comprimento em CENTÍMETROS da 2º reta do triângulo: '))
side3 = int(input(f'Digite o comprimento em CENTÍMETROS da 3º reta do triângulo: '))

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print(f'É POSSÍVEL formar um triângulo com as retas informadas!')
    if side1 == side2 == side3:
        print(f'O triângulo possui todos os lados IGUAIS, sendo assim é EQUILÁTERO.')
    elif side1 != side2 != side3 != side1:
        print(f'O triângulo possui todos os lados DIFERENTES, sendo assim é ESCALENO.')
    else:
        print(f'O triangulo possui dois lados IGUAIS e um DIFERENTE, sendo assim é ISÓSCELES.')
else:
    print(f'NÃO É POSSÍVEL formar um triângulo com as retas informadas!')
