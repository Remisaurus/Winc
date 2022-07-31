# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status):
    if location_of_the_cows == 'pasture':
        if weather == 'raining': return 'take cows to cowshed'
        if time_of_day == 'night': return 'take cows to cowshed'
    if cow_milking_status == True and location_of_the_cows == 'cowshed':
        return 'milk cows'
    elif cow_milking_status == True and location_of_the_cows == 'pasture':
        return """take cows to cowshed\nmilk cows\ntake cows back to pasture"""
    if slurry_tank == True:
        if location_of_the_cows == 'cowshed':
            if weather != 'sunny' or 'windy':
                return 'fertilize pasture'
        if location_of_the_cows == 'pasture':
            if weather != 'sunny' or 'windy':
                return """take cows to cowshed\nfertilize pasture\ntake cows back to pasture"""
    if grass_status == True and season == 'spring' and weather == 'sunny':
        if location_of_the_cows != 'pasture':
            return 'mow grass'
        elif location_of_the_cows == 'pasture':
            return """take cows to cowshed\nmow grass\ntake cows back to pasture"""
    else:
        return 'wait'
        
print(farm_action('sunny','day',True, 'pasture','spring',False,True))
