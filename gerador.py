import csv
import random
from faker import Faker

fake = Faker()

item_to_tag = {
    'Caneca': 'Utensilio',
    'Caneta': 'Utensilio',
    'Camisa': 'Vestuario',
    'Livro': 'Livro',
    'Laptop': 'Eletronico',
    'Telefone': 'Eletronico',
    'Mochila': 'Vestuario',
    'Relogio': 'Acessorio',
    'Chaveiro': 'Acessorio',
    'Garrafa': 'Utensilio'
}
conditions = ['horrivel', 'saudavel', 'bom estado', 'novo', 'usado']
approval = ['Aprovado', 'Reprovado']
clients = [fake.first_name() for _ in range(20)]
credits = [random.randint(500, 1000) for _ in range(20)]
dates = [fake.date_between(start_date='-1y', end_date='today') for _ in range(20)]


with open('itensregistrados.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for _ in range(20):
        item = random.choice(list(item_to_tag.keys()))
        tag = item_to_tag[item]
        row = [
            random.choice(clients),
            item,
            tag,
            random.choice(conditions),
            fake.bothify(text='???# - ###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'),
            random.choice([0, 1]),
            random.choice(approval),
            random.randint(0, 100),
            random.choice([0, 1]),
            random.choice(credits),
            random.choice(dates).strftime('%Y-%m-%d')
        ]
        writer.writerow(row)