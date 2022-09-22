import peewee
from models import *

db = peewee.SqliteDatabase(":memory:")

def create_tables():
    with db:
        Dish.create_table()
        Rating.create_table()
        Restaurant.create_table()
        Ingredient.create_table()

def add_some_dishes():
    meat = Ingredient.create(name = 'meat', is_vegetarian = False, is_vegan = False, is_glutenfree = True)
    meat.save()
    bread = Ingredient.create(name ='bread', is_vegetarian = True, is_vegan = True, is_glutenfree = False)
    bread.save()
    lettuce = Ingredient.create(name ='lettuce', is_vegetarian = True, is_vegan = True, is_glutenfree = True)
    lettuce.save()
    water = Ingredient.create(name ='water', is_vegetarian = True, is_vegan = True, is_glutenfree = True)
    water.save()  
    Burger = Dish.create(name ='Burger',served_at = 'Mac',price_in_cents = 300, ingredients = 'bread')
    Burger.save()
    '''
    Salad = Dish.create(name ='Salad', served_at = 'freshies',price_in_cents = 500, ingredients = lettuce)
    Salad.save()
    Soup = Dish.create(name ='Soup', served_at = 'Kitchen',price_in_cents = 400, ingredients = water)
    Soup.save()
    '''