"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

print(f'=====================')
print(f'10 Termos de uma PA')
print(f'=====================')
primeiro = int(input(f'Digite o primeiro termo: '))
razão = int(input(f'Digite a razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' -> ')
print(f'Acabou')
