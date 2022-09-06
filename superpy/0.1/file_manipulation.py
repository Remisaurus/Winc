import os
import csv
import datetime

from stock_manipulation import product

# Constants for directories and files used in the code
CURRENT_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
CURRENT_STOCK_FILE = os.path.join(DATA_DIR, 'current_stock.csv')
BUY_DATUMS_FILE = os.path.join(DATA_DIR, 'buy_datums.csv')
SET_DATE_FILE = os.path.join(DATA_DIR, 'set_date.txt')

# function to make a data directory if not already present.
def dir_maker():
    if os.path.isdir(DATA_DIR):
        print("data directory is present in current working directory")
    else:    
        os.mkdir(DATA_DIR)
        print("data directory was absent, and new one created")
        
# function to create data files if they are not already present. if all are present statement is made.        
def file_maker():
    if  os.path.isfile(CURRENT_STOCK_FILE):
        print('previous save file is present.')
    else:
        if not os.path.isfile(CURRENT_STOCK_FILE):
            with open(CURRENT_STOCK_FILE, 'w') as boss:
                print('current stock save file created')
    if  os.path.isfile(BUY_DATUMS_FILE):
        print('previous buy date save file is present.')
    else:
        if not os.path.isfile(BUY_DATUMS_FILE):
            with open(BUY_DATUMS_FILE, 'w') as boss:
                print('buy date save file created')
           
# function to write a simple txt file stating the program's set date if it does not exist already.                
def time_file_maker():
    if not os.path.isfile(SET_DATE_FILE):
            with open(SET_DATE_FILE, 'w') as boss:
                boss.write('now')
            print('Date set file created')

# function to reset time file.
# not tested with pytest
def reset_time():
    with open(SET_DATE_FILE, 'w') as boss:
        boss.write('now')
    
# function to replace the set date file with a new set date.
# not tested with pytest
def set_date(days):
    with open(SET_DATE_FILE, 'w') as boss:
        boss.write(str(days))
 
# function to delete all old data files and reinstate blank files (reset).
# not tested with pytest               
def reset_data():
    dir_maker()
    for all in os.listdir(DATA_DIR):
        os.remove(os.path.join(DATA_DIR, all))
    print('All files in data directory deleted.')
    file_maker()
    time_file_maker()

# this function deletes the old save files, and saves the inner dictionary to new save files
def overwrite_CSV(dict):
    if os.path.isfile(CURRENT_STOCK_FILE):
        os.remove(CURRENT_STOCK_FILE)
        print('Old file removed.')
    if os.path.isfile(BUY_DATUMS_FILE):
        os.remove(BUY_DATUMS_FILE)
        print('Old file removed.')
    file_maker()
    with open(BUY_DATUMS_FILE, 'w', newline='') as boss:
        writer = csv.writer(boss, delimiter=',')
        for every in dict:
            templist = []
            for it in dict[every].buy_datums:
                if type(it) == type(datetime.datetime.now()):
                    stringit = it.strftime("%d-%m-%Y")
                else:
                    stringit = it
                templist.append(stringit)
                templist.append(dict[every].buy_datums[it])    
            writer.writerow([templist])
    with open(CURRENT_STOCK_FILE, 'w', newline='') as boss:
        writer = csv.writer(boss, delimiter=';')
        for all in dict:   
            # (['id', 'name', 'quantity', 'buy price', 'buy datums', 'expiry date', 'sell status', 'sell quantity', 'sell price', 'sell date'])
            writer.writerow([dict[all].id, dict[all].name , dict[all].quantity, dict[all].buy_price, \
                'check other save file', dict[all].expiry_date.strftime("%d-%m-%Y"), dict[all].sell_status, dict[all].sell_quantity, \
                dict[all].sell_price, dict[all].sell_date])
    print('Saved.')
            
def load_CSV(dict):
    saved_buy_dates = {}
    with open(CURRENT_STOCK_FILE, 'r') as boss:
            reader = csv.reader(boss, delimiter = ';')
            for row in reader:
                dict[int(row[0])] = product(int(row[0]), row[1], int(row[2]), int(row[3]), row[5], \
                datetime.datetime.strptime(row[5], '%d-%m-%Y'), bool(row[6]), row[7], row[8], row[9])
                print(datetime.datetime.strptime(row[5], '%d-%m-%Y'))
                print(type(datetime.datetime.strptime(row[5], '%d-%m-%Y')))
               
    print('file loaded.')
            