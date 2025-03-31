# ATENÇÃO: Código via AI

import csv

# 1. Criar o arquivo dados.csv
with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Idade'])
    escritor.writerow(['Ana', 25])
    escritor.writerow(['Bruno', 30])
    escritor.writerow(['Carla', 22])
    escritor.writerow(['Daniel', 28])
    escritor.writerow(['Eduardo', 35])

# 2. Ler o arquivo dados.csv e armazenar os dados em uma lista
dados = []
with open('dados.csv', 'r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        dados.append(linha)

# Solicitar ao usuário para digitar um nome
nome_digitado = input("Digite um nome: ")

# Verificar se o nome digitado está na lista
encontrado = False
for pessoa in dados:
    if pessoa['Nome'] == nome_digitado:
        encontrado = True
        idade = int(pessoa['Idade'])
        print(f"Idade de {nome_digitado}: {idade}")

        # Verificar se é a pessoa mais velha
        mais_velho = True
        for outra_pessoa in dados:
            if int(outra_pessoa['Idade']) > idade:
                mais_velho = False
                break
        if mais_velho:
            print(f"{nome_digitado} é a pessoa mais velha da lista.")
        else:
            print(f"{nome_digitado} não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print(f"O nome {nome_digitado} não foi encontrado na lista.")