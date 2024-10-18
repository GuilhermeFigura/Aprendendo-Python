"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

nome = str(input(f'Digite um nome: ')).upper().strip()
nome_sem_espaço = nome.replace(" ", "") # Remove os espaços
inverso = nome_sem_espaço[::-1] # Inverte a string de trás para frente

if nome_sem_espaço == inverso:
    print(f'O inverso de {nome} é {inverso} \n'
          f'Sendo assim temos um PALÍNDROMOS.')
else:
    print(f'O inverso de {nome} é {inverso} \n'
          f'Sendo assim NÃO temos um PALÍNDROMOS.')
