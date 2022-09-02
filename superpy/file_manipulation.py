import os

# Constants for directories and files used in the code
CURRENT_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
AQUIRED_FILE = os.path.join(DATA_DIR, 'aquired.csv')
EXPIRED_FILE = os.path.join(DATA_DIR, 'expired.csv')
SOLD_FILE = os.path.join(DATA_DIR, 'sold.csv')
CURRENT_STOCK_FILE = os.path.join(DATA_DIR, 'current_stock.csv')
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
    if  os.path.isfile(AQUIRED_FILE) and os.path.isfile(EXPIRED_FILE) and os.path.isfile(SOLD_FILE) and os.path.isfile(CURRENT_STOCK_FILE):
        print('previous files are present.')
    else:
        if not os.path.isfile(AQUIRED_FILE):
            with open(AQUIRED_FILE, 'w') as boss:
                print('aquired file created')
        if not os.path.isfile(EXPIRED_FILE):
            with open(EXPIRED_FILE, 'w') as boss:
                print('expired file created')
        if not os.path.isfile(SOLD_FILE):
            with open(SOLD_FILE, 'w') as boss:
                print('sold file created')
        if not os.path.isfile(CURRENT_STOCK_FILE):
            with open(CURRENT_STOCK_FILE, 'w') as boss:
                print('current stock file created')
                
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
    
    
    '''
    with open(file_manipulation.AQUIRED_FILE, mode='w') as csv_file:
        fieldnames = ['product_name', 'date_of_aquisition', 'birth_month']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
        '''
    
    