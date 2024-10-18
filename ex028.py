"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""
import random
import time

print(f'*** JOGO DA SORTE ***')
jogador = int(input(f'Digite um número entre 0 e 5: '))
computador = random.randint(0, 5)
print(f'PROCESSANDO...')
time.sleep(3)

if jogador == computador:
    print(f'Parabéns, você adivinhou o número da sorte!')
else:
    print(f'PUTZ, Você errou o número da sorte!')
print(f'O número da sorte era {computador}.')
