import pandas as pd

# import cards and customer csv
cards = pd.read_csv('data/seeds_db/cards.csv')
customers = pd.read_csv('data/seeds_db/customers.csv')

# merge both dataframes where customer.id == card.customer_id

merged = pd.merge(customers, cards, left_on='id', right_on='customer_id')

# save csv

merged.to_csv('data/seeds_db/merged.csv', index=False)