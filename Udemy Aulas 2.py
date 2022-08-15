"""
num1 = input('Primeiro numero')
num2 = input('Segundo numero')
if num1 > num2:
    print(f'O numero {num1} é maior que {num2}')
elif num1 < num2:
    print(f'O numero {num2} é maior que {num1}')
else:
    print(f'O numero {num1} e o numero {num2} sao iguais')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if not n1 > n2:
    print(f'{n2} é maior que {n1}')
else:
    print(f'{n1} é maior que {n2}')
r= abs(n1-n2)
print(f'O diferencial absoluto entre os valores é {r}')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 < n2:
    print(f'{n2} é maior que {n1}')
elif n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print('Os números são iguais')
"""
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
NF = (nota1 + nota2) / 2
if not nota1 > 0:
    print(f'{nota1} é invalida')
elif not nota2 > 0:
    print(f'{nota2} é inválida')
elif nota1 > 10:
    print(f'{nota1} é uma nota inválida, por favor a corriga!')
elif not nota2 < 10:
    print(f'{nota2} é uma nota inválida, por favor a corriga!')
else:
    print(f'As notas {nota1} e {nota2} são válidas!')

print(f'Suas notas são {nota1} e {nota2} e sua média é {NF}')

if not NF > 6:
    print('Você foi reprovado')
else:
    print('Você foi aprovado')