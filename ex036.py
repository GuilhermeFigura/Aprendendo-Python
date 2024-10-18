""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. """
casa = float(input(f'Qual o valor da casa? R$ '))
salário = float(input(f'Qual o valor do seu salário? R$ '))
anos = float(input(f'Em quantos anos você irá pagar o empréstimo? '))
máximo = salário * 0.30
prestação = casa / (anos * 12)

if máximo > prestação:
    print(f'O valor máximo da prestação é R$ {prestação:.2f} e o seu salário é compatível.\nEmpréstimo APROVADO!')
else:
    print(f'O valor máximo da prestação é  R$ {prestação:.2f} e o seu salário NÃO é compatível. Empréstimo REPROVADO!')
    print(f'O máximo da sua renda é R$ {máximo:.2f}')
