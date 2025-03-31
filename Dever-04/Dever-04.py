import pandas as pd
import random

frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]
frutas_unicas = set(frutas)

with open('minhas_frutas.txt', 'w') as arquivo:
    for fruta in frutas:
        quantidade = random.randint(0, 100)  
        arquivo.write(f"{fruta},{quantidade}\n")
        
df = pd.read_csv('minhas_frutas.txt', header=None, names=['Fruta', 'Quantidade'])
df_agrupado = df.groupby('Fruta')['Quantidade'].sum().reset_index()

print("\nDataFrame com as frutas e quantidades somadas:")
print(df_agrupado)