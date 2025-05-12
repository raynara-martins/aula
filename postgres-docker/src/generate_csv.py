import pandas as pd
import random

df = pd.DataFrame({
    "id": range(50),
    "value": [random.randint(1, 100) for _ in range(50)]
})

csv_path = '/usr/src/app/dados/data.csv'
df.to_csv(csv_path, index=False)

print("CSV gerado com sucesso!")
print(df)  
