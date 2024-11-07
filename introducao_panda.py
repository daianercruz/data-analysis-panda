import pandas as pd

df = pd.read_csv("csv/gapminder.csv")

# Vizualizando as 5 primeiras linhas
print(df.head(5))

# Vizualizando as 10 primeiras linhas
print(df.head(10))

# Obtendo total de linhas e colunas
print(df.shape)

print(df.dtypes)

print(df.columns)

print(df.tail())

#Apresenta as ultimas 15 linhas
print(df.tail(15))


print(df.describe())


#Apresenta os continentes
print(df['continent'].unique())


print(df.groupby("year")["lifeExp"].mean())


#Media do PIB
print(df["gdpPercap"].mean())


#Somda do PIB
print(df["gdpPercap"].sum())