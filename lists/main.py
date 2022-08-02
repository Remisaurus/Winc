# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

#current assignment
from numbers import Integral


winlist=['jaws', 'star wars: episode iv - a new hope', 'e.t. the extra-terrestrial', 'memoirs of a geisha']
def mixs(num):
        try:
            ele = int(num)
            return (0, ele, '')
        except ValueError:
            return (1, num, '')
def alphabetical_order(filmlist):
   
    filmlist.sort(key = mixs)
    return filmlist

def won_golden_globe(filmname):
    if filmname.lower() in winlist: return True 
    else: return False
    
def remove_toto_albums(overpop):
    if 'Fahrenheit' in overpop: overpop.remove('Fahrenheit')
    if 'The Seventh One' in overpop: overpop.remove('The Seventh One')
    if 'Toto XX' in overpop: overpop.remove('Toto XX')
    if 'Falling in Between' in overpop: overpop.remove('Falling in Between')
    if 'Toto XIV' in overpop: overpop.remove('Toto XIV')
    if 'Old Is New' in overpop: overpop.remove('Old Is New')
    return overpop
         

'''

Use this information: Wikipedia -- Joseph Williams (musician)
It is not certain that all of Joseph's Toto albums are in the list received by remove_toto_albums, but they might! Don't let your script run into any errors.
Joseph did not inherit his dad's sloppiness with capitalization, so his Toto albums would be listed correctly.
Search the web on how to remove an item from a list by value.
'''
alphabetical_order([5, 1, 5, 'c' ,'b' ,'a'])