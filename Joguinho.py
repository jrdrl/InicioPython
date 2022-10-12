secret = 'chainsaw'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('É permitido apenas uma letra por vez')
        continue

    digitadas.append(letra)

    if letra in secret:
        print(f'A letra "{letra}" se encontra na palavra secreta. ')
    else:
        print(f'A letra "{letra}" não se encontra na palavra secreta.')
        digitadas.pop()

    secret_temp = ''

    for letra_secret in secret:
        if letra_secret in digitadas:
            secret_temp += letra_secret
        else:
            secret_temp += '#'

    if secret_temp == secret:
        print(f'Você ganhou !!! A palavra era : {secret}')
        break
    else:
        print(f'A palavra se encontra assim no momento:{secret_temp}')

    if letra not in secret:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
