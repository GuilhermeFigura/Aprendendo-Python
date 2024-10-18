#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input(f'Informe a temperatura em ºC: '))
fahrenheit = (celsius * 1.8) + 32
print(f'A temperatura de {celsius}ºC corresponde a {fahrenheit}ºF!')
