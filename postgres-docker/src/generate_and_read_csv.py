import pandas as pd
import random

numeros = [random.randint(1, 100) for _ in range(10)]
df = pd.DataFrame({'numeros_aleatorios': numeros})
csv_path = "/usr/src/app/dados/numeros.csv"
df.to_csv(csv_path, index=False)
print(f"Arquivo CSV gerado em {csv_path}")

df_lido = pd.read_csv(csv_path)
print("Conteúdo do CSV:")
print(df_lido)
