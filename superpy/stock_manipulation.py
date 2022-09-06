import file_manipulation
import date_manipulation

# id will be a number unique to every product.
# products will become objects with this class.
class product():
    def __init__(self, id, name, quantity, buy_price, buy_date, expiry_date, sell_status, sell_quantity = 0, \
        sell_price = 0, sell_date = date_manipulation.get_date(9999, 12, 31)):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.buy_price = buy_price
        self.buy_date = buy_date
        self.expiry_date = expiry_date
        self.sell_status = sell_status
        self.sell_quantity = sell_quantity
        self.sell_price = sell_price
        self.sell_date = sell_date

# dictionary containing all products as objects.
products = {}

# function that checks if product is already in dictionary.
def product_exists(argument_product_name):
    for product in products:
        if products[product].name == argument_product_name:
            return True
    return False
        
# function that gives the id(s) of the product(s) as a list if it is already in the dictionary,
# or returns False if not found.
def product_id_checker(argument_product_name):
    temp_list = []
    for product in products:
        if products[product].name == argument_product_name:
                temp_list.append(products[product].id)                     
    if len(temp_list) == 0:
        return False
    else:
        return temp_list

# function that returns a new unique id (highest +1)
def get_new_id():
    counter = 0
    for every in products:
        if products[every].id > counter:
            counter = products[every].id
    return counter + 1

# function to add stock to the inventory (needs 4 arguments) 
def add_stock(product_name, quantity, buy_price, expiry_date):
    sell_status = 'False'
    # products can be set as sold after they are added.
    new_id = get_new_id()
    buy_date = date_manipulation.get_date_set() 
    # programs set date is aquisition date for all added stock.
    products[new_id] = product(new_id, product_name, quantity, buy_price, buy_date, expiry_date, sell_status)

# function to remove ALL items with the same name from stock (sold and bought both)                  
def removing_stock(product_name):
    to_remove_list = product_id_checker(product_name)
    if to_remove_list == False:
        return 'not found'
    else:
        for id in to_remove_list:
            del products[id]
            
def print_current_stock(): #requires more logic
    print('id'.ljust(10) + 'name'.ljust(20) + 'quantity'.rjust(20) +'expiration date'.rjust(50))
    if len(products) == 0:
        print('')
        print('The stock seems to be empty')
        print('')
    else:
        count = 0 
        for product in products:
            if products[product].quantity > 0:
                product_expiry = products[product].expiry_date
                if len(products[product].name) > 18:
                    adapted_name = products[product].name[0:16] + '...'
                else:
                    adapted_name = products[product].name
                print (f'{products[product].id} '.ljust(10) + f'{adapted_name} '.ljust(20)\
                    + f'{products[product].quantity} '.rjust(20) + f'{product_expiry}'.rjust(50))
            else:
                count += 1
                if count > len(products):
                    print('')
                    print('The stock seems to be empty')
                    print('')
                else:
                    continue
                
def print_current_sales():
    print('function not implemented yet')
 
# Refers inner dictionary to be saved
def overwrite_to_CSV_file():
    file_manipulation.overwrite_CSV(products)
    
# Refers inner dictionary to be loaded
def load_from_CSV_file():
    file_manipulation.load_CSV(products)
    
    