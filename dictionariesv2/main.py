# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
   # passport = {'name':name, 'date_of_birth':date_of_birth, 'place_of_birth':place_of_birth, 'height':height, 'nationality':nationality}
    passport = dict(name=name, date_of_birth=date_of_birth, place_of_birth=place_of_birth, height=height, nationality=nationality)
    # print(passport)
    return passport

# ^^^ part 1 ^^^

def add_stamp(passport, country):
    passport['stamps']=country
    return passport
# not sure why this was already sufficient, but it passed the tests.

# ^^^ part 2 ^^^

def add_biometric_data(passport, name, biodata, date):
    print(passport, name, biodata, date)
    biometric = {name:{'date':date, 'value': biodata}}
    # print(biometric)
    if not 'biometric' in passport:
        passport['biometric']=biometric
    else:
        passport['biometric'][name]={'date':date, 'value': biodata}
    return passport
   
   # ^^^ that was part 3 ^^^
   
