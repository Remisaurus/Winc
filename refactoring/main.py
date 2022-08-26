__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# start of classes

specialist_list = None
homeowner_list = None

class specialist():
    def __init__(self, selfname, name, profession, hometown, price_per_hour):
        self.selfname = selfname
        self.name = name
        self.profession = profession
        self.hometown = hometown
        self.price_per_hour = price_per_hour
        global specialist_list
        if specialist_list == None:
            specialist_list = []
            specialist_list.append(self.selfname)
        else:
            specialist_list.append(self.selfname)
        
    def identify(self):
        print(f'I am {self.name}')
        print(f'I am from {self.hometown}')
        print(f'I am a specialist that works as {self.profession}')
        print(f'My price per hour would be {self.price_per_hour}')
        print(f'you can access me with : {self.selfname}')
        
class homeowner():
    def __init__(self, selfname, name, needs, adress, hometown):
        self.selfname = selfname
        self.name = name
        self.needs = needs
        self.adress = adress
        self.hometown = hometown
        self.contract_possibility_list = []
        global homeowner_list
        if homeowner_list == None:
            homeowner_list = []
            homeowner_list.append(self.selfname)
        else:
            homeowner_list.append(self.selfname)
        
    def identify(self):
       print(f'I am {self.name}')
       print(f'I live on {self.adress} in {self.hometown}')
       print(f'I am in need of {self.needs}')
       print(f'you can access me with : {self.selfname}')
       print(f'My possible matches with specialist(s) are :{self.contract_possibility_list}')
       
# end of classes
# start of data addition

# add data in this form:
# for specialists: unique_shortname = specialist(unique_shortname, name, profession, hometown, price_per_hour)
# for homeowners: unique_shortname = homeowner(unique_shortname, name, needs, adress, hometown)
# if the specific data is unknown, '-' must be used
# typeo's are not allowed! double check if neccessary! also all in strings ('' around word)!
       
alice = specialist('alice','Alice Aliceville','electrician','-', '-')
bob = specialist('bob','Bob Bobsville','painter','-', '-')
craig = specialist('craig','Craig Craigsville','plumber','-', '-')
alice2 = specialist('alice2', 'alice the second', 'electrician','somewhere else','-15')

alfred = homeowner('alfred', 'Alfred Alfredson', ['painter', 'plumber'], 'Alfredslane 123', '-')
bert = homeowner('bert', 'Bert Bertson', ['plumber'], 'Bertslane 231', '-')
candice = homeowner('candice', 'Candice Candicedottir', ['electrician', 'painter'], 'Candicelane 312', '-')
test = homeowner('test', 'Schraal Test Figuur', ['plumber','plumber','plumber','electrician','painter'],'Doos op brak terrein', 'buitenveld')

# end of data addition
# start of logics

def make_match_list(owner, need):
    for specialist in specialist_list:
        if globals()[specialist].profession == need:
            globals()[owner].contract_possibility_list.append({globals()[specialist].name : globals()[specialist].price_per_hour})


for owner in homeowner_list:
    for need in locals()[owner].needs:
        make_match_list(owner, need)

# end of logics
# N.B.
# logic can be added to find the best possible contract, this however requires a lot more data about the specialists.
# with the amount of data given there is little else to be done then giving the price per hour with the possible contracts.
# in this case even that information is not there.
# use .identify() on any instance to see most of their data

# following are a few lines to check/test the code
for person in specialist_list:
    locals()[person].identify()
    print('')

for owner in homeowner_list:
    locals()[owner].identify()
    print('')
    
# This file has been created as an exercize and should not be considered as serious