import pandas as pd

df = pd.read_csv('Produto.csv' , encoding='latin1')
media_estoque = df['quantidade_estoque'].mean()
print(media_estoque)