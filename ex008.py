# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input(f'Digite um uma distância em metros: '))
cm = medida / 0.01
mm = medida / 0.001
print(f'A conversão de distância de {medida} metros para centímetros é {cm}cm e para milímetros é {mm}mm')
