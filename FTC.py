num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'O número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'{num}É primo')
else:
    print(f'{num}Não é primo')
