__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import * #will also initialize database as db in memory
import peewee

'''
The code can break easily if not provided with correct data (ids for instance).

if a list is returned it can often not be fed into a next function.

for this excersize, all exchanges result in multiple items ids, there is no duplicate check.  

some arguments of the premade functions have the same name as made model attributes, \
since it does not appear to cause problems for the functionality they have not been renamed.

There has not been done any extensive testing on this code, \
and therefore a large quantity of small problems can be expected.
'''

def main():
    print('Check the main() function for test possibilities.')
    # test_it()

# function where functionality can be tested
def test_it():
    create_tables()
    populate_test_database(10)
    search('useless')
    list_products_per_tag(1)
    add_product_to_catalog(4, 'Eggs')
    update_stock(fetch_product_id('Eggs'), 25)
    purchase_product(fetch_product_id('Eggs'), 2, 22)
    list_user_products(4)
    remove_product(fetch_product_id('crappy drawing')) # removes ALL instances of crappy drawing
    list_user_products(2)
    
# Searches for a term, if no results are found in the name it continues to search tags and then description.
# A list with the results is returned.
def search(term):
    search_list = []
    search1 = product.select().where(product.name.contains(f'{term}'))
    for each in search1:
        print(f'results have been found in the name of: {each.name}')
        search_list.append(each)
    if len(search_list) == 0:
        search2 = product.select().join(producttags).join(tag).where(tag.descriptive_tag.contains(f'{term}'))
        for each in search2:
            print(f'results have been found in the descriptive tags of: {each.name}')
            search_list.append(each)
        if len(search_list) == 0:
            search3 = product.select().where(product.description.contains(f'{term}'))
            for each in search3:
                print(f'results have been found in the description of: {each.name}')
                search_list.append(each)
    return(search_list)

# Returns a list of items owned by a person with a particular id. Also prints some relevant data.
def list_user_products(user_id):
    product_list = []
    these = product.select().where(product.owner == user_id)
    this_guy = fetch_user_last_name(user_id)
    for every in these:
        print(f'Mister {this_guy} owns a quantity of: {every.quantity} of the product: {every.name}')
        product_list.append(every)
        if len(product_list) == 0:
            print('No products found')
            return 'No products found'
    return product_list
  
# prints and returns a list of items with a certain tag. (requires tag_id)
def list_products_per_tag(tag_id):
    product_list = []
    this = product.select().join(producttags).join(tag).where(tag.tag_id == tag_id)
    for every in this:
        print(f'The tag has been found on the product: {every.name}.')
        product_list.append(every)
    if len(product_list) == 0:
        print('No products found')
        return 'No products found'
    return product_list

# adds a product with stated name and default values to the database, the owner will be the user with user_id.
def add_product_to_catalog(user_id, product_name):
    add = make_new_product_number()
    add = product.create(name = product_name, owner = user_id)
    add.save()
    
# updates the quantity of the product with product_id  
# momentarily only works with single ids and not with lists  
def update_stock(product_id, new_quantity):
    update_this = product.select().where(product.product_id == product_id)
    for this in update_this:
        this.quantity = new_quantity
        this.save()
        print('quantity updated')
        return 'quantity updated'
    print('quantity update failed')

# user with buyer_id purchases a quantity of products with product_id
# no lists can be added in any of the arguments.
def purchase_product(product_id, buyer_id, quantity = 1):
    bought_item = product.select().where(product.product_id == product_id)
    for The_item in bought_item:
        seller = The_item.owner
        transaction_number = make_new_transaction_number()
        if The_item.quantity < quantity:
            print('transaction failed. quantity insufficient.')
            return 'transaction failed. quantity insufficient.'
        elif The_item.quantity == quantity:
            The_item.owner = buyer_id
            The_item.save()
            transaction_number = transaction.create(sold_item = The_item, sold_by = seller, bought_by = buyer_id, \
                quantity_sold = quantity, sold_for_price_in_cents = The_item.price_in_cents)
            transaction_number.save()
            print('Transaction succeeded.')
            return 'transaction succeeded.'
        elif The_item.quantity > quantity:
            The_item.quantity -= quantity
            The_item.save()
            transaction_number = transaction.create(sold_item = The_item, sold_by = seller, bought_by = buyer_id, \
                quantity_sold = quantity, sold_for_price_in_cents = The_item.price_in_cents)
            transaction_number.save()
            Part_of_it = make_new_product_number()
            Part_of_it = product.create(name = The_item.name, owner = buyer_id, price_in_cents = The_item.price_in_cents, \
                quantity = quantity, description = The_item.description, descriptive_tags = The_item.descriptive_tags)
            Part_of_it.save()
            print('transaction succeeded.')
            return 'transaction succeeded.'

# function to remove product(s). requires a product id or a list of product ids.
def remove_product(product_id):
    if isinstance(product_id, list): 
        for all in product_id:
            del_this = product.select().where(product.product_id == all)
            for every in del_this:
                every.delete_instance(recursive = True)
    else:
        del_this =product.select().where(product.product_id == product_id)
        for every in del_this:
            every.delete_instance(recursive = True)
    print('deleted')
        
    
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
    
# makes a new unique product number \
# (works until 300 000 products are numbered, some code should be added/changed after that point has been reached)
def make_new_product_number():
    largest_number = product.select(peewee.fn.MAX(product.product_id)).scalar()
    return largest_number + 5005
        
# makes a new unique transaction number
def make_new_transaction_number():
    largest_number = transaction.select(peewee.fn.MAX(transaction.transaction_id)).scalar()
    return largest_number + 305005

# to create the table framework (not neccessary when loading a previously saved file)
def create_tables():
    db.create_tables([tag, user, product, transaction, producttags])
    
# creates a number of users with differing last name, each will receive a test sheet product and 2 crappy drawings.
# (max 999)
def populate_test_database(number):
    if number < 10:
        print('populate with a number between 10-999 please.')
        return 'populate with a number between 10-999 please.'
    if number > 999:
        print('populate with a number between 10-999 please.')
        return 'populate with a number between 10-999 please.' 
    The_tag = tag.create()
    The_tag.save()  
    Another_tag = tag.create(descriptive_tag = 'neither a tag')
    Another_tag.save()
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
        all.descriptive_tags.add(The_tag)
        all.descriptive_tags.add(Another_tag)
        all.save()
    for all in range(3002, 3007):
        all = transaction.create(sold_item = all-3000, sold_by = all-3000, bought_by = all-3001, \
            sold_for_price_in_cents = 100)
        all.save()

if __name__ == "__main__":
    main()