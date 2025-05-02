import pandas as pd
from BTrees.OOBTree import OOBTree
import random
import timeit

# Завантаження даних
df = pd.read_csv('generated_items_data.csv')
# Створення структур
tree = OOBTree()
dictionary = {}

# Функції для додавання
def add_item_to_tree(tree, item):
    tree[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price']
    }

# def add_item_to_tree(tree, item):
#     price = item['Price']
#     if price not in tree:
#         tree[price] = []
#     tree[price].append(item)


def add_item_to_dict(d, item):
    d[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price']
    }
# def add_item_to_dict(d, item):
#     price = item['Price']
#     if price not in d:
#         d[price] = []
#     d[price].append(item)


# Завантаження товарів
count = 0
for _, row in df.iterrows():
    item = row.to_dict()
    add_item_to_tree(tree, item)
    add_item_to_dict(dictionary, item)
    count += 1
print(f"Додано записів: {count}")

# Функції діапазонного запиту
def range_query_tree(tree, min_price, max_price):
    result = []
    for price, items in tree.items(min_price, max_price):
        result.extend(items)
    return result


def range_query_dict(d, min_price, max_price):
    result = []
    for price in d:
        if min_price <= price <= max_price:
            result.extend(d[price])
    return result


# Створення 100 випадкових діапазонів

# price_ranges = [
#     (random.uniform(10, 50), random.uniform(51, 100))
#     for _ in range(100)
# ]

price_ranges = [
    tuple(sorted([random.uniform(10, 100), random.uniform(10, 100)]))
    for _ in range(100)
]

# Обгортки для timeit
def run_range_queries_tree():
    for r in price_ranges:
        range_query_tree(tree, r[0], r[1])

def run_range_queries_dict():
    for r in price_ranges:
        range_query_dict(dictionary, r[0], r[1])

# Вимірювання часу
tree_time = timeit.timeit(run_range_queries_tree, number=1)
dict_time = timeit.timeit(run_range_queries_dict, number=1)

# Результати
print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
