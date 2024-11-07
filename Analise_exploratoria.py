import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')



df = pd.read_excel("Planilhas/AdventureWorks.xlsx")

print(df.head())

#Quantidade de linhas e colunas
print(df.shape)

#Verificando os tipos de dados
print(df.dtypes)


#Qual o custo Total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo
     

print(df.head(1))

#Qual o custo Total?
round(df["custo"].sum(), 2)
     


df["lucro"]  = df["Valor Venda"] - df["custo"] 
     

print(df.head(1))

#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");
plt.show()

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");
plt.show()

df_2009 = df[df["Data Venda"].dt.year == 2009]
     
print(df_2009.head())

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");
plt.show()


df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');
plt.show()

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');
plt.show()

print(df["Tempo_envio"].describe())


