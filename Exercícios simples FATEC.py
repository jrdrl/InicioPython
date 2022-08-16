"""
# Insira 5 numeros e mostre a soma entre eles : Soma os números no alcance ex num ='10' ... 9+10= 19
num = int(input('Insira um número: '))
soma = 0
if num > 0:
    for i in range(num+1):
        soma = soma + i
        print(f" Para numero: {i} a soma é: {soma} ")
    print(f'A soma dos números {num} é {soma}')
elif num < 0:
    print('A soma é para números positivos')

--------------------------------------------------------------------------------
# Soma os algoritmos num = '10' Ex(1+0) 10 = 1
soma = 0
b = str(num)  # Transformo em str para poder usar posição. Ex: "b[1] = 2"
for i in range(len(b)):
    soma += int(b[i])
print('O resultado da soma é {}'.format(soma))
---------------------------------------------------------------------------------
"""
