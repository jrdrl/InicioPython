import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Questão
Quem são os 10 principais país exportadores de semicondutores?

Quem são os 10 principais país importadores de semicondutores?

Qual o papel do Brasil?
Trade Value (US$)
Reporter
Import*
Export*
*TradeFlow
Year
"""
# Importar a base de dados
contrade = pd.read_csv('UnContrade.csv')
contrade = contrade.rename(columns={'Trade Flow': 'TradeFlow'})
contrade = contrade.rename(columns={'Trade Value (US$)': 'TradeValueUS'})

# Visualização da base de dados
pd.set_option('display.max_columns', None)
print(contrade)
print('-' * 100)
# Importação dos países: gráfico dos valores e % de atuação do mercado e top 10
imp = contrade[['Year', 'Reporter', 'TradeFlow', 'TradeValueUS']]
data1 = [2000]
Tf = ['Import']
impd = imp[imp.Year.isin(data1)]
impd = impd[impd.TradeFlow.isin(Tf)]
print(impd)
print(impd.sort_values(by=['TradeValueUS'], ascending=False).head(10))

print('-' * 100)
# Grafico 1: Imp
plt.figure(figsize=(8, 6))

sns.set_palette('pastel')
impd = sns.barplot(x='Reporter', y='TradeValueUS', data=impd,
                   order=impd.sort_values('TradeValueUS', ascending=False).Reporter,
                   palette='Greens_d')

for i in impd.patches:
    impd.annotate(i.get_height(),
                  (i.get_x() + i.get_width() / 2, i.get_height()),
                  ha='center', va='baseline', fontsize=6, color='black', xytext=(0, 1),
                  textcoords='offset points')

plt.grid(True, color="grey", linewidth="0.8", linestyle="dashed")

impd.set_xticklabels(impd.get_xticklabels(), rotation=45, ha='right')
plt.title('Rank 10 de importação em US$')
plt.xlabel('Países')
plt.ylabel('Total em US$ importados')
plt.show()

print('-' * 100)
# Exportação dos países: gráfico dos valores e % de atuação do mercado e top 10
