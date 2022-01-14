# Analisando Dados Excel - Python

A ideia da aplicação é analisar a base de dados 'csv', e observar o porquê de uma empresa fictícia de **telecom** estar com um **churn** de mais de 26% dos clientes.

Para visualizar a Base de Dados: <a href="https://raw.githubusercontent.com/satoosan/Analise-Dados-Excel/542a09c318b44ee9993c489f48e57f7c964d0010/telecom_users.csv">telecom_users.csv</a>

**Com o botão direito do mouse, selecione a opção salvar como, para visualizar o arquivo no Excel**.

## 

## Sobre o Projeto
- Foi utilizado a lib **pandas**, para análise e tratamento de dados
- Foi utilizado a lib **plotly.express**, para criação dos gráficos em formatos de Histograma

**obs**: Algumas das libs necessita de serem instaladas, dependendo do ambiente em que esteja utilizando.
```Python
# Para instalacao do pandas
pip install pandas

# Para intalacao do plotly
pip install plotly
```

Imagens de Alguns Gráficos, utilizando o comando:
```Python
grafico = px.histogram(tabela, x=coluna, color='Churn')
grafico.show()  # Mostra o Grafico
```
<div>
<img src="https://cdn.discordapp.com/attachments/897304698468565022/931341159471656990/newplot.png" width="350px">
<img src="https://cdn.discordapp.com/attachments/897304698468565022/931341437738561626/newplot_1.png" width="350px">
<div>

##

### Créditos
- <a href="https://www.youtube.com/c/HashtagPrograma%C3%A7%C3%A3o">Hasgtag Lira</a>
