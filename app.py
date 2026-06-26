import pandas as pd

# Dados fictícios
dados = {
    "nome": [
        "Ana Silva",
        "Bruno Souza",
        "Carla Oliveira",
        "Diego Santos",
        "Fernanda Lima"
    ],
    "genero": [
        "Feminino",
        "Masculino",
        "Feminino",
        "Masculino",
        "Feminino"
    ],
    "idade": [
        25,
        32,
        28,
        40,
        35
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)

# Exportando para CSV
df.to_csv("pessoas_fake.csv", index=False, encoding="utf-8-sig")

print("\nArquivo 'pessoas_fake.csv' criado com sucesso!")

print("novo teste")
print("novooo")
