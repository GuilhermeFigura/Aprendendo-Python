"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
– Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER """

from datetime import date

year = int(input(f'Digite o seu ano de nascimento: '))
age = date.today().year - year

if age <= 9:
    print(f'O atleta possui {age} anos e sua categoria é MIRIM.')
elif age <= 14:
    print(f'O atleta possui {age} anos e sua categoria é INFANTIL')
elif age <= 19:
    print(f'O atleta possui {age} anos e sua categoria é JÚNIOR')
elif age <= 25:
    print(f'O atleta possui {age} anos e sua categoria é SÊNIOR')
elif age > 25:
    print(f'O atleta possui {age} anos e sua categoria é MASTER')
