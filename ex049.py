""" Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""


print('==== TABUADA ====')
número = int(input(f'Digite a tabuada que deseja: '))
tabuada = 0

for c in range(1, 11):
    print(f'{número} x {c} = {número * c}')
