# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
dias = int(input(f'Informe por quantos dias o carro foi alugado? '))
km = float(input(f'Informe quantos km foram percorridos? '))
custototal = (dias * 60) + (km * 0.15)
print(f'O preço total a pagar é R$ {custototal:.2f}!')
