"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu resultado!
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input(f'Digite o seu peso em (KG): '))
altura = float(input(f'Digite a sua altura em (m): '))
imc = peso / (altura ** 2)

print(f'O seu IMC é {imc:.2f}')
if imc < 18.5:
    print(f'Você está ABAIXO do peso!')
elif 18.5 <= imc < 24.9:
    print(f'Você está no peso IDEAL!')
elif 25 <= imc < 29.9:
    print(f'Você está com SOBREPESO!')
elif 30 <= imc < 39.9:
    print(f'Você está com OBESIDADE!')
else:
    print(f'Você está com OBESIDADE MÓRBIDA!')
