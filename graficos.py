import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter

dados = pd.read_csv('itensregistrados.csv')
counter = Counter(dados['Nome do item'])

# Pegar os 10 itens mais comuns
itens_populares = counter.most_common(10)

# Separar os itens e suas contagens
itens, contagens = zip(*itens_populares)

# Criar uma figura e um conjunto de subtramas

fig, ax = plt.subplots(figsize=(10, 7))

# Criar um gráfico de barras com itens e contagens
ax.bar(itens, contagens, color='', edgecolor='blue')

# Adicionar títulos e rótulos
ax.set_title('Itens mais populares', fontsize=15, fontweight='bold')
ax.set_xlabel('Itens', fontsize=12)
ax.set_ylabel('Contagens', fontsize=12)

# Girar os rótulos do eixo x
plt.xticks(rotation=45)

# Mostrar o gráfico
plt.show()