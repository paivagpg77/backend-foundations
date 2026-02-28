import pandas as pd

tabela = pd.read_csv("ClientesBanco.csv")

tabela = tabela.dropna()
display(tabela.info())
display(tabela.describe().round(1))