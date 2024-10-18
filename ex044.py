""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros """

print(f'{" LOJA FIGURA ":=^40}')
produto = float(input(f'Informe o total das compras: R$ '))
pagamento = int(input(f'''===== Escolha a forma de pagamento =====
[1] À vista dinheiro/cheque
[2] À vistão no cartão
[3] Parcelado em 2x no cartão
[4] Parcelado em 3x ou mais no cartão
Qual é a opção? '''))

if pagamento == 1:
    print(f'O valor da compra à vista/cheque ficou em R$ {produto * 0.90} com 10% de desconto.')
elif pagamento == 2:
    print(f'O valor da compra à vista/cheque ficou em R$ {produto * 0.95} com 5% de desconto.')
elif pagamento == 3:
    print(f'O valor da compra no cartão ficou em R$ {produto} e foi parcela em 2x de R${produto / 2}')
else:
    parcelas = int(input(f'Informe a quantidade de parcelas: '))
    print(f'O valor total ficou em R$ {produto * 1.20} com JUROS de 20% e cada parcela ficará em R$ {(produto * 1.20) / parcelas:.2f}')
