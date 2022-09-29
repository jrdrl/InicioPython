"""
num = input('Insira um número aqui: ')

try:
    num = int(num)

except:
    print('O valor inserido não é um inteiro')


if num % 2 == 0:
    print('O número proposto é par')
else:
    print('O número proposto é impar')

hora = input('Que horas são? ')
hora = float(hora)

if 0 <= hora <= 11:
    print(f'Bom dia! São {hora:.2f} ')
if 12 <= hora <= 17:
    print(f'Boa tarde! São {hora:.2f}')
if 18 <= hora <= 23:
    print(f'Boa noite! São {hora:.2f}')

if hora >= 0 and not hora >= 11:
    print(f'Bom dia! São {hora:.2f}')
"""
nome = input('Insira seu nome:\n')

if not nome.isdecimal():
    if len(nome) <= 4:
        print('Nome curto')
    elif len(nome) >= 5 and not len(nome) > 6:
        print('Nome médio')
    elif len(nome) >= 7:
        print('Nome grande')
