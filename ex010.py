# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

reais = float(input(f'Quanto de dinheiro você tem na carteira? R$ '))
dólar = 3.27
print(f'A cotação dólar hoje está R$ {dólar}!\nSendo assim, você consegue comprar o total de US$ {reais/dólar:.2f}.')
