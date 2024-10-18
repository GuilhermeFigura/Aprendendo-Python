"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme a média atingida:"""

nota1 = float(input(f'Digite a PRIMEIRA nota: '))
nota2 = float(input(f'Digite a SEGUNDA nota: '))
média = (nota1 + nota2) / 2

print(f'O aluno tirou {nota1} e {nota2}! A nota média ficou em {média:.1f}!')
if média >= 7:
    print(f'O aluno está APROVADO!')
elif 7 > média >= 5:
    print(f'O aluno está RECUPERAÇÃO!')
elif média < 5:
    print(f'O aluno está REPROVADO!')
