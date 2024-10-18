# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input(f'Qual a largura da parede em metros? '))
altura = float(input(f'Qual a altura da parede em metros? '))
área = largura * altura
tinta = área / 2
print(f'A parede possui dimenção de {largura} x {altura} e área da parede é {área:.1f}m².')
print(f'Para píntar essa parede é necessário {tinta:.1f}l de tinta.')
