"""
Recebendo dados do usuário(básico)
"""
# Entrada de dados
print("Qual seu nome ? ")
nome = input()  # Entrada
# print('Seja bem-vindo(a) {0}'.format(nome))
# Formato antigo print("Seja bem-vindo(a) %s" % nome)
# Exemplo de print utilizado atualmente
print(f'Seja bem-vindo(a)! {nome}')
print("Qual sua idade?")
idade = input()
# Processamento de dados

# Saída de dados
# Formato antigo print("Ele(a) %s tem %s anos" % (nome, idade))
"""Duas ou mais variáveis necessita que se coloque dentro dos parenteses, vide linha 8 1V, vide linha 15 (2v)"""
# print('{0} tem {1} anos'.format(nome, idade))
# Exemplo print novo vide linhas 17 e 7
print(f'{nome} tem {idade} anos')

print(f'{nome} nasceu em {2022 - int(idade)}')
"""
Cast >> int(idade)
Cast é a conversão de um tipo de dado para outro
>>>> Todo dado recebido via input é do tipo string
Em python, string é tudo que estiver dentro de 'Aspas simples', "duplas", '''simples triplas''' e
duplas triplas
"""