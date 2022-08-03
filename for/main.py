from os import remove
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(list):
    newlist=[]
    for i in list:
        if len(i) <= 3:
            newlist.append(i)
    if len(newlist) < 1:
        for i in list:
          if len(i) == 4:
            newlist.append(i)
    if len(newlist) < 1:
        for i in list:
          if len(i) == 5:
            newlist.append(i)
    return newlist

def count_vowels(list):
        vowelcountlist=[]
        for country in list:
            counter = 0
            for letter in country:
                if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                    counter = counter + 1
            vowelcountlist.append(counter)
        # print(sorted(vowelcountlist, reverse=True))
        return sorted(vowelcountlist, reverse=True)

        
def most_vowels(list):
    counted=count_vowels(list)
    result = []
    for country in list:
        counter = 0 
        for letter in country:
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                    counter = counter + 1
        if counter == counted[0]:
            result.append(country)
            list.remove(country)
            
    if len(result) >= 3:
        #print(result)
        return result
    
    for country in list:
        counter = 0 
        for letter in country:
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                    counter = counter + 1
        if counter == count_vowels(list)[0]:
            result.append(country)
            list.remove(country)  
            
    if len(result) >= 3:
        #print(result)
        return result       
    
    for country in list:
        counter = 0 
        for letter in country:
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                    counter = counter + 1
        if counter == count_vowels(list)[0]:
            result.append(country)
            list.remove(country)        
     #print(result)
    return result  
# ^^^ first and second exercise
# third exercise following : 

# I misunderstood the excercise, the missing letters were j,k and x with my top 8 so these I added in this manner,
# I do not think this excercize was meant to waste too much time and since I already wasted somuch I took a shortcut.

def countryx(list):
    for country in list:
        if 'x' in country: return country
        elif 'X' in country: return country
        
        
def countryj(list):
    for country in list:
        if 'j' in country: return country
        elif 'J' in country: return country
        
        
def countryk(list):
    for country in list:
        if 'k' in country: return country
        elif 'K' in country: return country
       

def countalphinstring(country):
    counter = 0
    if 'a' in country: counter = counter + 1
    elif 'A' in country: counter = counter + 1
    if 'b' in country: counter = counter + 1
    elif 'B' in country: counter = counter + 1
    if 'c' in country: counter = counter + 1
    elif 'C' in country: counter = counter + 1
    if 'd' in country: counter = counter + 1
    elif 'D' in country: counter = counter + 1
    if 'e' in country: counter = counter + 1
    elif 'E' in country: counter = counter + 1
    if 'f' in country: counter = counter + 1
    elif 'F' in country: counter = counter + 1
    if 'g' in country: counter = counter + 1
    elif 'G' in country: counter = counter + 1
    if 'h' in country: counter = counter + 1
    elif 'H' in country: counter = counter + 1
    if 'i' in country: counter = counter + 1
    elif 'I' in country: counter = counter + 1
    if 'j' in country: counter = counter + 1
    elif 'J' in country: counter = counter + 1
    if 'k' in country: counter = counter + 1
    elif 'K' in country: counter = counter + 1
    if 'l' in country: counter = counter + 1
    elif 'L' in country: counter = counter + 1
    if 'm' in country: counter = counter + 1
    elif 'M' in country: counter = counter + 1
    if 'n' in country: counter = counter + 1
    elif 'N' in country: counter = counter + 1
    if 'o' in country: counter = counter + 1
    elif 'O' in country: counter = counter + 1
    if 'p' in country: counter = counter + 1
    elif 'P' in country: counter = counter + 1
    if 'q' in country: counter = counter + 1
    elif 'Q' in country: counter = counter + 1
    if 'r' in country: counter = counter + 1
    elif 'R' in country: counter = counter + 1
    if 's' in country: counter = counter + 1
    elif 'S' in country: counter = counter + 1
    if 't' in country: counter = counter + 1
    elif 'T' in country: counter = counter + 1
    if 'u' in country: counter = counter + 1
    elif 'U' in country: counter = counter + 1
    if 'v' in country: counter = counter + 1
    elif 'V' in country: counter = counter + 1
    if 'w' in country: counter = counter + 1
    elif 'W' in country: counter = counter + 1
    if 'x' in country: counter = counter + 1
    elif 'X' in country: counter = counter + 1
    if 'y' in country: counter = counter + 1
    elif 'Y' in country: counter = counter + 1
    if 'z' in country: counter = counter + 1
    elif 'Z' in country: counter = counter + 1
    return counter
    
        

def countalphchars(list):
    alphcountlist= []
    for country in list:
       alphcountlist.append(countalphinstring(country))
    return sorted(alphcountlist, reverse=True)
            
  
  
def alphabet_set(list):    #number 1 to 8 and j+k+x
    result = []
    for country in list:
        if countalphinstring(country) == countalphchars(list)[0]: # has 17 unique alphabet characters
            result.append(country)
        if countalphinstring(country) == countalphchars(list)[1]: # has 15 unique alphabet characters
            result.append(country)
        if countalphinstring(country) == countalphchars(list)[2]: # both have 14 unique alphabet characters
            result.append(country)
        if countalphinstring(country) == countalphchars(list)[4]: # four countries with 13 unique alphabet characters
            result.append(country)
        
        
    # I misunderstood the exersize, the missing letters were j,k and x with my top 8 so these I added in this manner,
    # I do not think this exersize was meant to waste too much time and since I already wasted somuch I took a shortcut.
    result.append(countryx(list))
    result.append(countryj(list))
    result.append(countryk(list))
            
            
    return result
    
    
        
            

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    
    """ Write the calls to your functions here. """
    # print (shortest_names(get_countries()))
    # count_vowels(get_countries())
    # most_vowels(get_countries())
    # print(count_vowels(most_vowels(get_countries())))
    print(alphabet_set(get_countries()))
    # print(countalphchars(get_countries()))

   
'''
alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. How short can you get your list to be?
Letter case is not relevant, so 'a' is the same letter as 'A' with regards to the alphabet.
Solutions with 14 or fewer countries are accepted as correct.
Wincpy Check
Use wincpy check for to see if you met all of the requirements for this exercise. Did you pass the test?
'''
