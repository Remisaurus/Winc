import models
import peewee
import datetime
import filefortests
from typing import List


__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"

db = peewee.SqliteDatabase(":memory:", pragmas={'foreign_keys': 1})
db.create_tables([models.Dish, models.Restaurant, models.Rating, models.Ingredient, models.DishIngredient])
filefortests.add_some_dishes()

def cheapest_dish() -> models.Dish:
    say_no_more = 0
    cheapest = models.Dish.select().where(models.Dish.price_in_cents == \
        models.Dish.select(peewee.fn.MIN(models.Dish.price_in_cents)).scalar())
    for cheapdish in cheapest:
        if say_no_more == 0:
            print(f'the cheapest dish seems to be:"{cheapdish.name}". It costs {cheapdish.price_in_cents} cents at {cheapdish.served_at.name}.')
            say_no_more = 1
        else:
            print(f'multiple results have been found with the price of {cheapdish.price_in_cents} cents. it includes the {cheapdish.name} from {cheapdish.served_at.name}. ')
    return cheapest

def vegetarian_dishes() -> List[models.Dish]:
    vegetarianish = []
    number = 0
    number2 = 0
    ask = models.Dish.select()
    for Dis in ask:
        for Ing in Dis.ingredients:
            number += 1
        for Ing in Dis.ingredients:
            if Ing.is_vegetarian == True:
                number2 += 1
                if number2 == number:
                    vegetarianish.append(Dis)
                    number = 0 
                    number2 = 0
                    print(f'{Dis.name} seems to be vegetarian. it is available at {Dis.served_at.name}')
                    break
                else:
                    continue
            else:
                number = 0
                number2 = 0
                break
    return vegetarianish

def best_average_rating() -> models.Restaurant:
    averages = []
    aks = models.Rating.select()
    for every in aks:
        averages.append(models.Rating.select(peewee.fn.AVG(models.Rating.rating)).where(models.Rating.restaurant == every.restaurant).scalar())
    for this in aks:
        if models.Rating.select(peewee.fn.AVG(models.Rating.rating)).where(models.Rating.restaurant == this.restaurant).scalar() == max(averages):
            return this.restaurant
        else:
            continue

def add_rating_to_restaurant() -> None:
    ff = models.Restaurant.select().where(models.Restaurant.id == 1)
    models.Rating.create(restaurant = ff, rating = 3, comment = 'blah')


def dinner_date_possible() -> List[models.Restaurant]:
    possibilities = []
    veganish = []
    number = 0
    number2 = 0
    ask = models.Dish.select()
    for Dis in ask:
        for Ing in Dis.ingredients:
            number += 1
            # counting number of ingredients.
        for Ing in Dis.ingredients:
            if Ing.is_vegan == True:
                number2 += 1
                if number2 == number:
                    veganish.append(Dis.served_at)
                    number = 0 
                    number2 = 0
                    print(f'{Dis.name} seems to be vegan. it is available at {Dis.served_at.name}')
                    break
                else:
                    continue
            else:
                number = 0
                number2 = 0
                break
    for vegandishplace in veganish:
        if vegandishplace.opening_time >= datetime.time(19,0,0) and vegandishplace.closing_time <= datetime.time(7,0,0):
            possibilities.append(vegandishplace)
    return possibilities
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    opening_time = peewee.TimeField()
    closing_time = peewee.TimeField()
    """

def add_dish_to_menu() -> models.Dish:
    myr = models.Restaurant.create(name = 'myr', open_since = datetime.date.today(),opening_time =datetime.datetime.now().time(),closing_time =datetime.datetime.now().time())
    myr.save()
    bread = models.Ingredient.create(name = 'bread', is_vegetarian = True, is_vegan = True, is_glutenfree = False)
    bread.save()
    cheese = models.Ingredient.create(name = 'cheese', is_vegetarian = True, is_vegan = False, is_glutenfree = True)
    cheese.save()
    Grilledcheese = models.Dish.create(name ='toastie', served_at = myr , price_in_cents = 250)
    Grilledcheese.ingredients.add(bread)
    Grilledcheese.ingredients.add(cheese)
    Grilledcheese.save()
    return Grilledcheese
