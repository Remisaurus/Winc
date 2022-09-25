import datetime
import peewee
from models import *

db = peewee.SqliteDatabase(":memory:", pragmas={'foreign_keys': 1})

def create_tab():
    with db:
        Dish.create_table()
        Rating.create_table()
        Restaurant.create_table()
        Ingredient.create_table()

def add_some_dishes():
    mac = Restaurant.create(name = 'mac', open_since = datetime.date.today(),opening_time =datetime.datetime.now().time(),closing_time =datetime.datetime.now().time())
    mac.save()
    freshies = Restaurant.create(name = 'freshies', open_since = datetime.date.today(),opening_time =datetime.datetime.now().time(),closing_time =datetime.datetime.now().time())
    freshies.save()
    Kitchen = Restaurant.create(name = 'Kitchen', open_since = datetime.date.today(),opening_time =datetime.datetime.now().time(),closing_time =datetime.datetime.now().time())
    Kitchen.save()
    meat = Ingredient.create(name = 'meat', is_vegetarian = False, is_vegan = False, is_glutenfree = True)
    meat.save()
    bread = Ingredient.create(name = 'bread', is_vegetarian = True, is_vegan = True, is_glutenfree = False)
    bread.save()
    lettuce = Ingredient.create(name = 'lettuce', is_vegetarian = True, is_vegan = True, is_glutenfree = True)
    lettuce.save()
    water = Ingredient.create(name ='water', is_vegetarian = True, is_vegan = True, is_glutenfree = True)
    water.save()  
    Burger = Dish.create( name ='Burger', served_at = mac , price_in_cents = 300)
    Burger.ingredients.add(bread)
    Burger.ingredients.add(meat)
    Burger.save()
    Salad = Dish.create(name ='Salad', served_at = freshies , price_in_cents = 300)
    Salad.ingredients.add(lettuce)
    Salad.save()
    Soup = Dish.create(name ='Soup', served_at = Kitchen , price_in_cents = 300)
    Soup.ingredients.add(water)
    Soup.ingredients.add(meat)
    Soup.save()
    one = Rating.create(restaurant = Kitchen, rating = 5, comment = 'bla')
    one.save()
    two = Rating.create(restaurant = Kitchen, rating = 4, comment = 'bla')
    two.save()
    three = Rating.create(restaurant = mac, rating = 5, comment = 'bla')
    three.save()
    four = Rating.create(restaurant = mac, rating = 1, comment = 'blabla')
    four.save()
    five = Rating.create(restaurant = freshies, rating = 4, comment = 'blablabla')
    five.save()
    
    
    
    



    

