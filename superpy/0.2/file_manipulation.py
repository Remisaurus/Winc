import os
import csv
import stock_manipulation

# Constants for directories and files used in the code
CURRENT_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
CURRENT_STOCK_FILE = os.path.join(DATA_DIR, 'current_stock.csv')
SET_DATE_FILE = os.path.join(DATA_DIR, 'set_date.txt')

# function to make a data directory if not already present.
def dir_maker():
    if os.path.isdir(DATA_DIR):
        print("data directory is present in current working directory")
    else:    
        os.mkdir(DATA_DIR)
        print("data directory was absent, and new one created")
        
# function to create data save file if it is not already present. if present statement is made.        
def file_maker():
    if  os.path.isfile(CURRENT_STOCK_FILE):
        print('Previous save file is present.')
    else:
        if not os.path.isfile(CURRENT_STOCK_FILE):
            with open(CURRENT_STOCK_FILE, 'w') as boss:
                print('New save file created')

# function to write a simple txt file stating the program's set date if it does not exist already.                
def time_file_maker():
    if not os.path.isfile(SET_DATE_FILE):
            with open(SET_DATE_FILE, 'w') as boss:
                boss.write('now')
            print('Date set file created')

# function to reset time file.
# not tested with pytest
def reset_time():
    if os.path.isfile(SET_DATE_FILE):
       os.remove(SET_DATE_FILE)
    with open(SET_DATE_FILE, 'w') as boss:
        boss.write('now')
    
# function to replace the set date with a new set date (and file).
# not tested with pytest
def set_date(days):
    if os.path.isfile(SET_DATE_FILE):
       os.remove(SET_DATE_FILE)
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
# not tested with pytest  
def overwrite_CSV(dict):
    if os.path.isfile(CURRENT_STOCK_FILE):
        os.remove(CURRENT_STOCK_FILE)
        print('Old save file removed.')
    file_maker()
    with open(CURRENT_STOCK_FILE, 'w', newline='') as boss:
        writer = csv.writer(boss, delimiter=';')
        for all in dict:
            writer.writerow([dict[all].id, dict[all].name , dict[all].quantity, dict[all].buy_price, \
                dict[all].buy_date, dict[all].expiry_date, dict[all].sell_status, \
                dict[all].sell_quantity, dict[all].sell_price, dict[all].sell_date])
    print('Saved.')

# This function loads the data in the CSV file, if valid, to the internal dictionary
# not tested with pytest  
def load_CSV(dict):
    file_maker()
    try:
        with open(CURRENT_STOCK_FILE, 'r') as boss:
            reader = csv.reader(boss, delimiter = ';')
            for row in reader:
                dict[int(row[0])] = stock_manipulation.product(int(row[0]), row[1], int(row[2]), float(row[3]), \
                   row[4], row[5], row[6], int(row[7]), float(row[8]), row[9])
        print('file loaded.')
    except ValueError:
        print('The save file seems to be corrupted. Not all saved data may be loaded.') 
        print('A reset is recommended.')


