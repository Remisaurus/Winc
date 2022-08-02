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


def count_unique_letters(string):
    for letter in string:
        counter=0
        if letter.isalpha():
            counter = counter + 1
            '''current excercise'''
            
  
  
def alphabet_set(list):
    print('something')

 
    
        
            

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    
    """ Write the calls to your functions here. """
    # print (shortest_names(get_countries()))
    # count_vowels(get_countries())
    # most_vowels(get_countries())
    # print(count_vowels(most_vowels(get_countries())))
    alphabet_set(get_countries())

   
'''
alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. How short can you get your list to be?
Letter case is not relevant, so 'a' is the same letter as 'A' with regards to the alphabet.
Solutions with 14 or fewer countries are accepted as correct.
Wincpy Check
Use wincpy check for to see if you met all of the requirements for this exercise. Did you pass the test?
'''
