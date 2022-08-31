# Make buy_datum proper dictionary!



import file_manipulation
import date_manipulation

# id will be a number unique to every product.
# products with the same name and different expiry dates will have different id numbers.

# products will become objects with this class.
class product():
    def __init__(self, id, name, quantity, buy_price, buy_date, expiry_date):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.buy_price = buy_price
        self.buy_datums = {buy_date:quantity}
        self.expiry_date = expiry_date

# dictionary containing all products as objects.
products = {}

# function that checks if product is already in dictionary.
def product_exists(argument_product_name):
    for product in products:
        if products[product].name == argument_product_name:
            return True
    return False

# function that checks if the expiry date of a new item is different than the one already in the dictionary.
def new_product_expiry_date_is_different(argument_product_name, argument_expiry_date):
    id = product_id_checker(argument_product_name)
    if products[id].expiry_date == argument_expiry_date:
        return False
    return True

# function that gives the id of the product if it already is in the dictionary and has the same expiry date.
# if the product is in the dictionary a check is made to see if the expiry dates are different, if they are,
# or the product is not in the dictionary, a new id is given for the product.
def product_id_checker_with_expiry_date(argument_product_name, argument_expiry_date):
    counter = 0
    for product in products:
        if products[product].name == argument_product_name:
            if new_product_expiry_date_is_different(argument_product_name, argument_expiry_date) == False:
                return products[product].id                      
        if products[product].id > counter:
            counter = products[product].id
    return counter + 1

# function that gives the id of the product if it is already in the dictionary,or
# creates a new id if it is not.
def product_id_checker(argument_product_name):
    counter = 0
    for product in products:
        if products[product].name == argument_product_name:
                return products[product].id                      
        if products[product].id > counter:
            counter = products[product].id
    return counter + 1

# function to add stock to the inventory (needs at least 4 arguments) 
def add_stock(product_name, quantity, buy_price, expiry_date):
    if product_exists(product_name):
        if new_product_expiry_date_is_different(product_name, expiry_date) == False:
            id = product_id_checker(product_name)            
            products[id].quantity += quantity
            new_buy_date = date_manipulation.get_date_set_datetime_form()
            products[id].buy_datums[new_buy_date] = quantity
        else:
            id = product_id_checker_with_expiry_date(product_name, expiry_date)
            buy_date = date_manipulation.get_date_set_datetime_form()
            products[id] = product(id, product_name, quantity, buy_price, buy_date, expiry_date)
    else:
        id = product_id_checker(product_name)
        buy_date = date_manipulation.get_date_set_datetime_form()
        products[id] = product(id, product_name, quantity, buy_price, buy_date, expiry_date)
        
    

