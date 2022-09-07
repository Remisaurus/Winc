




print('r' * 19)







'''
even = {1:2,3:4}

print(even)
print(even[1])

for every in even:
    print(every)
    print(even[every])
'''










'''
import os
import csv
import ast
import json
import datetime
CURRENT_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
CURRENT_STOCK_FILE = os.path.join(DATA_DIR, 'current_stock.csv')

with open(CURRENT_STOCK_FILE, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist", "dictionary"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins", {'no':'really', 'yes':'cool'}])
    writer.writerow([2, "Harry Potter", "Harry Potter", "nothing"])
    
print(ast.literal_eval("{'grr': 1}"))
'''