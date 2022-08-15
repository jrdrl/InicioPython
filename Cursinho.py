import pandas as pd
import win32com.client as win32

# Importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

print('-'*50)
# Faturamento por loja
Faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(Faturamento)

print('-'*50)
# Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-'*50)
# Ticket médio por produto
ticket_medio = (Faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

print('-'*50)
# Enviar e-mail com relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'Send to'
mail.Subject = 'Assunto (subject) Tentativa de email'
mail.HTMLBody = f"""
<p>Assunto em HTML</p>

<p> Segue o relatório de vendas de cada loja</p> 

<p>Faturamento por loja</p>
{Faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade de produtos vendidos por loja</p>
{quantidade.to_html(formatters={'Quantidade': '{:,} UN'.format})}

<p>Ticket médio</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Att,</p>
<p>Jarod</p>

"""
mail.Send()

print('Email enviado!')
