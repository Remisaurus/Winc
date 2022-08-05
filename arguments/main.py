# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# current assignment 05-08-2022
def bogusgreet(greeting):
    print(greeting)

def greet(name, greeting='not yet given'):
    if greeting =='not yet given':
        bogusgreet(f'Hello, {name}!')
    print(name, greeting)




'''

Part 1: Greet Template
Define a function greet in main.py that takes these arguments, in this order:

A name (str)
A greeting template (str). Set this template parameter to 'Hello, <name>!' by default.
greet should return a string where <name> in the greeting template is replaced by the name given in the first parameter. For example:

greet('Doc')
'Hello, Doc!'
greet('Bob', "What's up, <name>!")
"What's up, Bob!"
You do not need to handle the case where <name> is not in the greeting template string.

Part 2: Force
Read this up to and including "Example: how much force to hold an apple with a mass of 0.1 kg?":

Math Is Fun -- Gravity
You should now understand the formula:

force = mass × gravity

Open up this page for reference:

Surface Gravity of the Planets and the Sun
Write a function force that takes two arguments:

mass (float)
body (str), with 'earth' as its default. Your implementation should support all 11 bodies listed on the reference website given above (in lowercase). Make sure you process these bodies with the correlated gravity factor in a dictionary. Before using the gravity of a celestial body round its gravity factor to 1 decimal. You can "hardcode" this, for example: the gravity of Earth becomes 9.8.
The arguments should be named exactly as listed so that we can call them with keyword arguments. force should return the force that is exerted given the mass and body.

Part 3: Gravity
Read on from "But What Is Gravity?" on the same page as previously:

Math Is Fun -- Gravity
You should now understand the formula:

pull = G × ((m1×m2)/d2)

Recall that in Python you can express powers with **, for example: x5 would be x ** 5 in Python.

Write a function pull that takes three arguments:

m1 An object's mass in kg (float)
m2 Another object's mass in kg (float)
d Their distance in meters (float)
pull should return the gravitional pull that these two objects have on each other. You can test your function by entering in the examples given on the website
'''