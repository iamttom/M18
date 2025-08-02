
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

plt.figure(figsize=(10,5))
sns.lineplot(x="dia", y="venda", data=df)
plt.title("Preço da gasolina - SP - Julho 2021")
plt.xlabel("Dia")
plt.ylabel("Preço médio (R$)")
plt.savefig("gasolina.png")
