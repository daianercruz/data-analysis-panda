import pandas as pd


df1 = pd.read_excel("Planilhas/Aracaju.xlsx")
df2 = pd.read_excel("Planilhas/Natal.xlsx")
df3 = pd.read_excel("Planilhas/Recife.xlsx")
df4 = pd.read_excel("Planilhas/Salvador.xlsx")


print(df1.head())

#juntando os arquivos
df = pd.concat([df1, df2, df3, df4])

#Exibindo as 5 primeiras linhas
print(df.head())

#Exibindo as 5 ultimas linhas
print(df.tail())

#Alterando o tipo de dado da coluna Loja ID
df["LojaID"] = df["LojaID"].astype("object")

print(df["LojaID"])


#Consultar linhas com valores zerados
print(df.isnull().sum())

#Substituindo os valores zerados pela média
df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)

print(df["Vendas"])

#Deletando linhas que estejam com valores zerados em todas as colunas
df.dropna(how="all", inplace=True)

print(df.dropna)

#criando coluna de receita
df["Receita"]= df["Vendas"].mul(df["Qtde"])

print(df.head())


print(f" Retornando a maior receita: {df["Receita"].max()}")


print(f" Retornando a menor receita:{df["Receita"].min()}")

#Agrundando por cidade
df.groupby("Cidade")["Receita"].sum()

print(df.sort_values("Receita", ascending=False).head(15))


#Trabalhando com datas 

df["Data"] = df["Data"].astype("int64")
print(df.dtypes)


df["Data"] = pd.to_datetime(df["Data"])
print(df.dtypes)

# Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

print(df.sample(5))


# Retornando a data mais antiga
print(f"Retornando a data mais antiga:{df["Data"].min()}")

# Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))

# Criando a coluna de trimestre
df["trimestre_vendas"] = df["Data"].dt.quarter
print(df.sample(5))

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) &(df["Data"].dt.month == 3)]
     

print(vendas_marco_19)

