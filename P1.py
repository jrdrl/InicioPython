import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')
tabela_vendas = tabela_vendas.rename(columns={'ID Loja': 'IDLoja'})
# Visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

print('-' * 50)
# Faturamento por loja
Faturamento = tabela_vendas[['IDLoja', 'Valor Final']].groupby('IDLoja').sum()
print(Faturamento.sort_values(by=['Valor Final'], ascending=False))

print('-' * 50)
# Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['IDLoja', 'Quantidade']].groupby('IDLoja').sum()
print(quantidade.sort_values(by=['Quantidade'], ascending=False))

print('-' * 50)
# Ticket médio por produto
ticket_medio = (Faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio.sort_values(by=['Ticket Médio'], ascending=False))

print('-' * 50)

# Criando gráfico

plt.figure(figsize=(10, 5))
Faturamento['IDLoja'] = Faturamento.index  # Solução
fat = sns.barplot(x='IDLoja', y='Valor Final', data=Faturamento,
                  order=Faturamento.sort_values('Valor Final', ascending=False).IDLoja,
                  palette='Blues_d')

for i in fat.patches:
    fat.annotate(i.get_height(),
                 (i.get_x() + i.get_width() / 2, i.get_height()),
                 ha='center', va='baseline', fontsize=6, color='black', xytext=(0, 1),
                 textcoords='offset points')
fat.set_xticklabels(fat.get_xticklabels(), rotation=45, ha='right')
plt.title('Faturamento total recebido por loja')
plt.show()
