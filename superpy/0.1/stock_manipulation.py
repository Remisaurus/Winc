import file_manipulation
import date_manipulation

# id will be a number unique to every product.
# products with any difference in name, sell status, buy in price or expiry date will have different id numbers.

# products will become objects with this class.
class product():
    def __init__(self, id, name, quantity, buy_price, buy_date, expiry_date, sell_status, sell_quantity = 0, \
        sell_price = 0, sell_date = date_manipulation.get_date_form(9999, 12, 31).strftime("%d-%m-%Y")):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.buy_price = buy_price
        self.buy_datums = {buy_date:quantity}
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

# function that checks if an item is different than the one(s) found in the dictionary.
# returns True if product is new, returns id number of the product which it is similar to if not.
def new_product_is_different(argument_product_name, argument_expiry_date, argument_buy_price, argument_sell_status):
    id_list = product_id_checker(argument_product_name)
    temp_list = []
    for i in id_list:
        if products[i].expiry_date == argument_expiry_date and \
        products[i].buy_price == argument_buy_price and \
        products[i].sell_status == argument_sell_status:
                    temp_list.append(False)
        else:
            temp_list.append(True)
    for every in temp_list:
        if every == True:
            continue
        else:
            return id_list[temp_list[every]]
    return True
        
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

# function that returns a new unique id
def get_new_id():
    counter = 0
    for every in products:
        if products[every].id > counter:
            counter = products[every].id
    return counter + 1

# function to add stock to the inventory (needs at least 4 arguments) 
def add_stock(product_name, quantity, buy_price, expiry_date):
    sell_status = False
    # products can be set as sold after they are added.
    if product_exists(product_name) == True:
        if type(new_product_is_different(product_name, expiry_date, buy_price, sell_status)) == type(True):
            new_id = get_new_id()
            buy_date = date_manipulation.get_date_set_datetime_form() 
            # programs set date is aquisition date for all added stock.
            products[new_id] = product(new_id, product_name, quantity, buy_price, buy_date, expiry_date, sell_status)
        else:
            old_id = new_product_is_different(product_name, expiry_date, buy_price, sell_status)
            print(products[old_id].quantity)
            products[old_id].quantity += quantity
            buy_date = date_manipulation.get_date_set_datetime_form() 
            # programs set date is aquisition date for all added stock.
            products[old_id].buy_datums[buy_date] = quantity 
    else:
        new_id = get_new_id()
        buy_date = date_manipulation.get_date_set_datetime_form() 
        # programs set date is aquisition date for all added stock.
        products[new_id] = product(new_id, product_name, quantity, buy_price, buy_date, expiry_date, sell_status)
        
def removing_stock(product_name):
    to_remove_list = product_id_checker(product_name)
    if to_remove_list == False:
        return 'not found'
    else:
        for id in to_remove_list:
            del products[id]
            
def print_current_stock():
    print('id'.ljust(10) + 'name'.ljust(20) + 'quantity'.rjust(20) +'expiration date'.rjust(50))
    if len(products) == 0:
        print('')
        print('The stock seems to be empty')
        print('')
    else:
        count = 0 
        for product in products:
            if products[product].quantity > 0:
                product_expiry = products[product].expiry_date.strftime('%d-%m-%Y')
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

def overwrite_to_CSV_file():
    file_manipulation.overwrite_CSV(products)
    
def load_from_CSV_file():
    file_manipulation.load_CSV(products)
    
    