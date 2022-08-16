"""
#Ler o salário e o valor da prestação mensal se > 20% ==>  não consedido caso < que 20% Concedido
sal = float(input('Qual o total do salário recebido ? R$'))
Parcela = float(input('Qual o valor mensal que será debitado ? R$'))
Permitido = sal * 20/100

if Parcela > Permitido:
    print('O empréstimo não pode ser concedido pois ultrapassa 20% do seu salário')
    print(f'Salário de {sal} valor permitido {Permitido}')
else:
    print('Empréstimo condedido!')

# Receber altura e sexo de uma pessoa e calcule mostrando o peso ideal onde h corresponde a altura
# Homens (72.7*h) - 58
# Mulheres (62.1 * h) - 58

h = float(input('Informe sua altura ? '))
sx = str(input('Informe seu sexo[M/F]: ')).strip()

if sx in 'Mm':
    peso_idealm = float((72.7 * h) - 58)
    str(print('Seu peso ideal é {}'.format(peso_idealm)))
elif sx in 'Ff':
   peso_idealf = float((62.1 * h) - 58)
   str(print('Seu peso ideal é {}'.format(peso_idealf)))

# Escrever um programa que leia um numero positivo > que zero e some todos os algarismos

num = int(input('Insira o número a ser somado: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

soma = 0
a = 123
b = str(num)  # Transformo em str para poder usar posição. Ex: "b[1] = 2"
for i in range(len(b)):
    soma += int(b[i])
print('O resultado da soma é {}'.format(soma))

# Ler um numero inteiro se > 0 log se < 0 invalido
import math

num = float(input('Insira um número: '))

if num <= 0:
    print('Número é inválido, selecione outro!')
else:
    print(math.log(num))

# média ponderada de 3 notas primera e segunda peso 1 e 3a peso 2 , mostrar media e indicar ap ou rep >= 60
nota1 = float(input('Insura a primeira nota aqui: '))
peso1 = 1

nota2 = float(input('Insura a segunda nota aqui: '))
peso2 = 1

nota3 = float(input('Insura a terceira nota aqui: '))
peso3 = 2

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print('Sua média nas três avaliações é de {:.2f}'.format(media))

if media > 60:
    print('Aprovado'.upper())
else:
    print('Reprovado'.upper())

n = 1
P = 0
I = 0
while n <= 10:
    a = int(input())
    n = n + 1
    if a % 2 == 0:
        P = P + 1
    else:
        I = I + 1

print("A qtd de números pares é: ", P)
print("A qtd de números ímpares é: ", P)

"""