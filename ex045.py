""" Crie um programa que faça o computador jogar Jokenpô com você. """
import random

computador = random.randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input(f'''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? '''))
print(f'-=' * 14)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print(f'-=' * 14)

if jogador == computador:
    print(f'EMPATE!')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print(f'PARABÉNS, Jogador ganhou!')
else:
    print(f'PERDEU! Computador ganhou!')
