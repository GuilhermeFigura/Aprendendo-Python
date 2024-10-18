'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''

cidade = str(input(f'Digite a cidade que você nasceu: ')).strip()
cidade = cidade.upper()
print(f'{cidade[:5] == 'SANTO'}')
