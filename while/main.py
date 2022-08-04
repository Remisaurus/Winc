from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

# 1st assignment
def unique_koala_facts(num):
    unique_list =[]
    counter = 0
    while len(unique_list)<num:
        counter +=1
        new_round = random_koala_fact()
        if counter >= 1000:
            print('this is the thousand\'s time')
            print('result is: '+str(unique_list))
            break
        if new_round in unique_list:
            continue
        else: unique_list.append(new_round)
    else: print('the loop completed with result: '+str(unique_list))
    return unique_list

#second assignment
def num_joey_facts():
    ten_list = []
    unique_joey_list = []
    
    christmass=False
    while not christmass:
        new_round=random_koala_fact()
        if 'joey' in new_round:
            ten_list.append(new_round)
            if new_round not in unique_joey_list: unique_joey_list.append(new_round)
            if ten_list.count(new_round) >= 10: 
                print('the same fact has appeared ten times.')
                break
    else: print('christmass is here!')
    # print(unique_joey_list)
    return len(unique_joey_list)     

# Third assignment      
def koala_weight():
    koala_kg = 0
    while not koala_kg:
        round=random_koala_fact()
        if round.find('kg')>=1:
            # print(round)
            print(round[round.find('kg')-2:round.find('kg')])
            koala_kg=round[round.find('kg')-2:round.find('kg')]
    return int(koala_kg)    
if __name__ == "__main__":
    # print(random_koala_fact())
    # unique_koala_facts(10)
    # num_joey_facts()
    koala_weight()
''' 
koala_weight: somewhere in the data is a fact about how heavy a koala is. This function should return that weight in kilogram (kg) as an integer.
'''