# Importação de biblioetecas necessárias
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Criação de arquivo CSV
with open('imc_data.csv', 'w') as f:
    f.write("IMC,Obeso\n")  
    f.write("18.5,False\n")  
    f.write("22.0,False\n")  
    f.write("25.5,False\n")  
    f.write("27.8,False\n")  
    f.write("29.9,False\n")  
    f.write("30.1,True\n")   
    f.write("32.5,True\n")   
    f.write("35.0,True\n")   
    f.write("37.2,True\n")   
    f.write("40.0,True\n")   

# Visualização de arquivo CSV criado
data = pd.read_csv('imc_data.csv')
print(data)

# Dados para treinamento
X = data[['IMC']]  
y = data['Obeso'] 

# Criar e treinar o modelo
model = LogisticRegression()
model.fit(X, y)

print("Modelo treinado! Limite de decisão em IMC ≈ 30")

while True:
    try:
        novo_imc = float(input("\nDigite um IMC (ou 'sair' para encerrar): "))
        if novo_imc <= 0:
            print("IMC deve ser positivo!")
            continue
            
        # Previsão
        predicao = model.predict([[novo_imc]])
        
        if predicao[0]:
            print(f"IMC {novo_imc}: OBESO (True) - Cuidado com a saúde!")
        else:
            print(f"IMC {novo_imc}: NÃO OBESO (False) - Mantenha hábitos saudáveis!")
    
    except ValueError:
        print("Programa encerrado.")
        break