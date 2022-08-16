# Insira 5 numeros e mostre a soma entre eles
n = 1
P = 0
I = 0
while n <= 5:
    a = int(input())
    n = n + 1
    if a % 2 == 0:
        P = P + 1
    else:
        I = I + 1
print(f'A qtde de numeros impares é {I}')
print(f'A qtde de números pares é {P}')
