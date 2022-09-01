from unicodedata import name


class object():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
dit = object('iets', 8)

x = input('push enter: ')

dic = {'gewoon':dit}

print(dic)
print(dic['gewoon'].name)
print(dic['gewoon'].quantity)
x = 2
dic['gewoon'].quantity += x
print(dic['gewoon'].quantity)
