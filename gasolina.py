
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10,5))
sns.lineplot(data=df, x='dia', y='venda')
plt.title('Preço Médio da Gasolina - Julho/2021 (SP)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.savefig('gasolina.png')
