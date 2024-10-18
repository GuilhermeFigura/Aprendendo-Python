"""Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é
a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

atual = date.today().year
ano = int(input(f'Qual o ANO de nascimento? '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual} !!')

if idade < 18:
    print(f'Ainda não chegou a época de se alistar ao serviço militar! Faltam {18 - idade} ano(s).')
elif idade == 18:
    print(f'Chegou a hora de se alistar ao serviço militar, você possui {idade} anos.')
elif idade > 18:
    print(f'Você perdeu o prazo para se alistar em {idade - 18} ano(s).')
