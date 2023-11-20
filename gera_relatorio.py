from datetime import datetime
from typing import List
import csv
from collections import Counter

class Transaction:
    def __init__(self, date, product_category: str, total_value: float, items_exchanged: int, popular_products: List[str]):
        self.date = date
        self.product_category = product_category
        self.total_value = total_value
        self.items_exchanged = items_exchanged
        self.popular_products = popular_products
class Manager:
    def __init__(self, transactions_file):
        self.transactions = []
        with open(transactions_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                date = datetime.strptime(row[-1], '%Y-%m-%d')
                product_category = row[2]
                total_value = float(row[-2])
                items_exchanged = int(row[5])
                donated_products = row[1].split(',')
                self.transactions.append(Transaction(date, product_category, total_value, items_exchanged, donated_products))

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def generate_report(self, start_date, end_date, category, min_total_value):
        if category:
            filtered_transactions = [t for t in self.transactions 
                                     if start_date <= t.date <= end_date
                                     and t.product_category == category and
                                     t.total_value >= min_total_value]
        else:
            filtered_transactions = [t for t in self.transactions 
                                     if start_date <= t.date <= end_date
                                     and t.total_value >= min_total_value]

        total_sales = sum(t.total_value for t in filtered_transactions)
        total_items_exchanged = sum(t.items_exchanged for t in filtered_transactions)
        popular_products = [product for t in filtered_transactions for product in t.popular_products]
            
        product_counts = Counter(popular_products)
        product_counts = {product: count for product, count in product_counts.items() if count > 1}

        return {
            'total_sales': total_sales,
            'total_items_exchanged': total_items_exchanged,
            'product_counts': product_counts
        }
manager = Manager('itensregistrados.csv')

# Define the start and end dates for the report
# Generate a report for a specific category and minimum total value

# start_date = datetime.strptime('2022-01-01', '%Y-%m-%d')
# end_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
# var = None
# report = manager.generate_report(start_date, end_date,var, 0)

# # Print the report
# print(report)

