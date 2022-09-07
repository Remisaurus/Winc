import file_manipulation
import date_manipulation

# id will be a number unique to every product.
# products will become objects with this class.
class product():
    def __init__(self, id, name, quantity, buy_price, buy_date, expiry_date, sell_status = False, \
        sell_quantity = 0, sell_price = 0, sell_date = '31-12-9999'):
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

# dictionary containing all products as objects with their id as key.
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

# function that checks howmuch stock of a particular name is available for selling on the set date        
def sellable_stock(name):
    stock_counter = 0
    if product_id_checker(name) == False:
        print(f'could not find {name} in inventory')
    else:
        name_list = product_id_checker(name)
        for entry in name_list:
            if date_manipulation.earlier_check(products[entry].expiry_date) == False:
                if date_manipulation.later_check(products[entry].buy_date) == False:
                    stock_counter += products[entry].quantity
    return stock_counter

# function that prints the current stock of sellable items.         
def print_current_stock(): #retain the number of spaces in the string below.
    print('name                                             |'.ljust(0) + 'quantity'.rjust(10))
    if len(products) == 0:
        print('')
        print('The stock seems to be empty')
        print('')
    else:
        count = 0 
        done_list = []
        for product in products:
            if products[product].name in done_list:
                continue
            if products[product].quantity > 0 and sellable_stock(products[product].name) > 0:
                done_list.append(products[product].name)
                amount = sellable_stock(products[product].name)
                if len(products[product].name) > 49:
                    adapted_name = products[product].name[0:46] + '...|'
                else:
                    adapted_name = products[product].name + (' ' * (49 - len(products[product].name)) + '|')
                print (f'{adapted_name} '.ljust(0) + f'{amount} '.rjust(10))
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
    
# function that prints a list of expired items for the set date.
# in addition this function will return the amount of losses due to expired items.    
def print_expired_items():
    loops_check = 0
    loss_count = 0
    for product in products:
        if date_manipulation.earlier_check(products[product].expiry_date) == False:
            continue
        else:
            if products[product].quantity > 0:
                loops_check += 1
                print(f'Item {products[product].name} has expired on {products[product].expiry_date}.\
 this involves an item quantity of {products[product].quantity} and a loss of\
 {products[product].quantity * products[product].buy_price}.')
                loss_count = loss_count + products[product].quantity * products[product].buy_price
    if loops_check == 0:
        print('')
        print('No items are expired at this set date')
        return 'no loss'
    print(f'The total losses from expired items is: {loss_count}.')
    return loss_count

# function that sells product from list aquired the earliest (first in first out) until full quantity is sold.
# function is second in line of selling product and represents the recallable part.
def sell_product(list, quantity, sell_price):
    if quantity == 0:
        return 'done'
    this_one = 'nothing yet'
    this_date = date_manipulation.get_date_datetime_form(9999, 12, 31)
    for idea in list:
        if date_manipulation.earlier_check(products[idea].expiry_date) == False:
            if date_manipulation.compare_dates(date_manipulation.get_string_in_date_form(products[idea].buy_date), this_date) == False:
                this_one = idea
                this_date = date_manipulation.get_string_in_date_form(products[idea].buy_date)
    if quantity >= products[this_one].quantity:
        quantity -= products[this_one].quantity
        products[this_one].sell_quantity = products[this_one].quantity
        products[this_one].quantity = 0
        products[this_one].sell_price = sell_price
        products[this_one].sell_status = True
        products[this_one].sell_date = date_manipulation.get_date_set()
        list.remove(this_one)
        sell_product(list, quantity, sell_price)
    if quantity < products[this_one].quantity:
        new_id = get_new_id()
        products[new_id] = product(new_id, products[this_one].name, 0, products[this_one].buy_price,\
                                    products[this_one].buy_date, products[this_one].expiry_date, True, \
                                    quantity, sell_price, date_manipulation.get_date_set())
        products[this_one].quantity -= quantity
        return 'done'
        
# function to sell stock from the inventory (needs 3 arguments)        
def selling_stock(product_name, quantity, sell_price):
    if sellable_stock(product_name) < quantity:
        print('Not enough stock with that name to sell this quantity.')
        return 'not enough inventory'
    else:
        list = product_id_checker(product_name)
        sell_product(list, quantity, sell_price)
        return 'done'        
 
# Refers inner dictionary to be saved
def overwrite_to_CSV_file():
    file_manipulation.overwrite_CSV(products)
    
# Refers inner dictionary to be loaded
def load_from_CSV_file():
    file_manipulation.load_CSV(products)
    
    