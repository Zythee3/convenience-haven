import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
from menu import *
from gera_relatorio import *
import matplotlib.dates as mdates

def graphics_1(report):

    dados = report['total_sales']
    counter = Counter(report['product_counts'])
    itens_populares = counter.most_common(10)

    if itens_populares:
        itens, contagens = zip(*itens_populares)

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.bar(itens, contagens, color='skyblue', edgecolor='blue')
    ax.set_title('Itens mais populares', fontsize=15, fontweight='bold')
    ax.set_xlabel('Itens', fontsize=12)
    ax.set_ylabel('Contagens', fontsize=12)
    plt.xticks(rotation=90)
    plt.show()
    
def graphics_2(start_date):
    df = pd.read_csv('itensregistrados.csv')
    df['Data da Transacao'] = pd.to_datetime(df['Data da Transacao']).dt.date

    start_date = start_date.date()
    df = df[df['Data da Transacao'] >= start_date]
    df = df.sort_values('Data da Transacao')

    item_counts = df.groupby('Data da Transacao')['Nome do item'].count()

    item_counts.plot(kind='bar', figsize=(10, 7))

    ax = plt.gca()
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.title('Contagem de Itens por Data')
    plt.xlabel('Data')
    plt.ylabel('Contagem de Itens')
    plt.xticks(rotation=90)
    plt.show()