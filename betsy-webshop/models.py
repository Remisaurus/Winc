import peewee 
import datetime

db = peewee.SqliteDatabase(":memory:", pragmas={'foreign_keys': 1})

class overclass(peewee.Model):
    
    class Meta:
        database = db

class user(overclass):
    # Every user can own multiple products through the products model. 
    # The products have a relational key to users stating their owner.
    user_id = peewee.AutoField()
    first_name = peewee.TextField(default = 'John or Jane')
    last_name = peewee.TextField(default = 'Doe') 
    address_1 = peewee.TextField(default = 'Streetroad')   
    address_2 = peewee.CharField(default = '1gr')
    address_3 = peewee.CharField(default = 'Posty123')
    address_4 = peewee.TextField(default = 'Villagetown')
    billing_info = peewee.CharField(default = 'a 1/2 card')
        
class product(overclass):
    product_id = peewee.AutoField()
    name = peewee.CharField(default = 'unnamed product')
    owner = peewee.ForeignKeyField(user, backref = 'owned_by')
    price_in_cents = peewee.IntegerField(default = 100) # since the field is integer and represents cents, the possibility of rounding errors is small.
    quantity = peewee.IntegerField(default = 1)
    description = peewee.CharField(default = 'useless')
    descriptive_tags = peewee.CharField(unique=True, null=True)
       
class transaction(overclass):
    transaction_id = peewee.AutoField()
    sold_item = peewee.ForeignKeyField(product)
    sold_by = peewee.ForeignKeyField(user)
    bought_by = peewee.ForeignKeyField(user)
    quantity_sold = peewee.IntegerField(default = 1)
    sold_for_price_in_cents = peewee.IntegerField()
    sell_date = peewee.DateField(default = datetime.date.today())