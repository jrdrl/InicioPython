import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

print('-'*50)
# Faturamento por loja
Faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(Faturamento.sort_values(by=['Valor Final'], ascending=False))

print('-'*50)
# Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade.sort_values(by=['Quantidade'], ascending=False))

print('-'*50)
# Ticket médio por produto
ticket_medio = (Faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio.sort_values(by=['Ticket Médio'], ascending=False))

print('-'*50)

# grafico 1 hist simples
Faturamento['Valor Final'].hist()
# plt.show()

# produtos value
produtos = tabela_vendas['Produto']
print(produtos.value_counts())
