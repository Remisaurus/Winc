__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import peewee
import datetime 


def main():
    create_tables()
    populate_test_database(10)
    print(search('useless'))

# Searches for a term, if no results are found in the name it continues to search tags and then description.
# A list with the results is returned.
def search(term):
    search_list = []
    search1 = product.select().where(product.name.contains(f'{term}'))
    for each in search1:
        search_list.append(each)
    if len(search_list) == 0:
        search2 = product.select().where(product.descriptive_tags.contains(f'{term}'))
        for each in search2:
            search_list.append(each)
        if len(search_list) == 0:
            search3 = product.select().where(product.description.contains(f'{term}'))
            for each in search3:
                search_list.append(each)
    return(search_list)

def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...
    
# to get product id by name (list if more than one) 
def fetch_product_id(name):
    id_list = []
    fetching = product.select().where(product.name == name)
    for allnames in fetching:
        id_list.append(allnames.product_id)
    if len(id_list) == 0:
        return 'not found'
    elif len(id_list) == 1:
        return id_list[0]
    else:
        return id_list
    
# to get product's name by id:    
def fetch_product_name(id):
    fetching = product.select().where(product.product_id == id)
    for whatever_is_in_fetching in fetching:
        return whatever_is_in_fetching.name

# to get user id by name (list if more than one) 
def fetch_user_id(last_name):
    id_list = []
    fetching = user.select().where(user.last_name == last_name)
    for allnames in fetching:
        id_list.append(allnames.user_id)
    if len(id_list) == 0:
        return 'not found'
    elif len(id_list) == 1:
        return id_list[0]
    else:
        return id_list

# to get user's last name by id:
def fetch_user_last_name(id):
    fetching = user.select().where(user.user_id == id)
    for whatever_is_in_fetching in fetching:
        return whatever_is_in_fetching.last_name

# to get transaction id for item(name) (list if more than one) 
def fetch_transaction_id(item):
    id_list = []
    second_id_list = []
    the_fetched_id_list = product.select().where(product.name == item)
    for every in the_fetched_id_list:
        second_id_list.append(every.product_id)   
    for all_ids in second_id_list:
        fetching = transaction.select().where(transaction.sold_item == all_ids)
        for allsells in fetching:
            id_list.append(allsells.transaction_id)
    if len(id_list) == 0:
        return 'not found'
    elif len(id_list) == 1:
        return id_list[0]
    else:
        return id_list

# to get item sold by id:
def fetch_transaction_item(id):
    fetching = transaction.select().where(transaction.transaction_id == id)
    for whatever_is_in_fetching in fetching:
        this_one = product.select().where(product.product_id == whatever_is_in_fetching)
        for name in this_one:
            return name.name

# to create the table framework (not neccessary when loading a previously saved file)
def create_tables():
    db.create_tables([user, product, transaction])
    
# creates a number of users with differing last name, each will receive a test sheet product and 2 crappy drawings.
# (max 999)
def populate_test_database(number):
    if number < 10:
        print('populate with a number between 10-999 please.')
        return 'populate with a number between 10-999 please.'
    if number > 999:
        print('populate with a number between 10-999 please.')
        return 'populate with a number between 10-999 please.'    
    for all in range(number+1):
        if all == 0:
            continue
        all = user.create(last_name = f'Doe number {all}')
        all.save()
    for all in range(1001, number+1001):
        all = product.create(name = 'test sheet', owner = all-1000)
        all.save()
    for all in range(2001, number+2001):
        all = product.create(name = 'crappy drawing', quantity = 2, owner = all-2000)
        all.save()
    for all in range(3002, 3007):
        all = transaction.create(sold_item = all-3000, sold_by = all-3000, bought_by = all-3001, \
            sold_for_price_in_cents = 100)
        all.save()
        
'''
 mac = Restaurant.create(name = 'mac', open_since = datetime.date.today(),opening_time =datetime.datetime.now().time(),closing_time =datetime.datetime.now().time())
    mac.save()

    transaction_id = peewee.AutoField()
    sold_item = peewee.ForeignKeyField(product)
    sold_by = peewee.ForeignKeyField(user)
    bought_by = peewee.ForeignKeyField(user)
    quantity_sold = peewee.IntegerField(default = 1)
    sold_for_price_in_cents = peewee.IntegerField()
    sell_date = peewee.DateField(default = datetime.date.today())
'''

if __name__ == "__main__":
    main()