import pandas as pd
import plotly.express as px

# Importar Base de Dados
tabela = pd.read_csv('telecom_users.csv')

# Visualizar Base de Dados
# print(tabela)

# Tratamento de Dados
# remover coluna inutil
# axis = 0 -> linha
# axis = 1 -> coluna
tabela = tabela.drop('Unnamed: 0', axis=1)
# print(tabela)

# Valores reconhecidos de forma errada
# object -> texto
# int -> numero inteiro | float -> numero com casa decimal
# print(tabela.info())

# Casting text for float
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# Tratar valores vazios
tabela = tabela.dropna(how="all", axis=1)  # excluir as colunas vazias
tabela = tabela.dropna(how="any", axis=0)  # excluir as linhas vazias
# print(tabela.info())

# Analise Inicial
# print(tabela['Churn'].value_counts())
# print(tabela['Churn'].value_counts(normalize=True).map(
#     '{:.1%}'.format))  # Formatado em Porcentagem

# Analise detalhada dos clientes
for coluna in tabela.columns:
    # Cria um grafico do tipo histograma
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()  # Mostra o Grafico
