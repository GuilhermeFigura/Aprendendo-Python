'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
nome1 = str(input(f'Digite o 1º nome: '))
nome2 = str(input(f'Digite o 2º nome: '))
nome3 = str(input(f'Digite o 3º nome: '))
nome4 = str(input(f'Digite o 4º nome: '))
sorteio = [nome1, nome2, nome3, nome4]
print(f'O aluno sorteado para apagar o quadro é {random.choice(sorteio)}')
