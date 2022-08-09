# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1 : 
def greet(name='empty', greeting='Hello, <name>!'):
    if name == 'empty':
        print('unhandled exeption')
        return ''
    if '<name>' in greeting:
        print(greeting[0:greeting.find('<name>')]+name+greeting[greeting.find('<name>')+6:])
        return(greeting[0:greeting.find('<name>')]+name+greeting[greeting.find('<name>')+6:])
    print(greeting+' '+name)
    return(greeting+' '+name)

# part 2 :
def force(mass, body='earth'):
    if body == 'sun':
        print(mass*274) 
        return mass*274
    if body == 'jupiter':
        print(mass*24.9) 
        return mass*24.9
    if body == 'neptune':
        print(mass*11.2) 
        return mass*11.2
    if body == 'saturn':
        print(mass*10.4) 
        return mass*10.4
    if body == 'earth':
        print(mass*9.8) 
        return mass*9.8
    if body == 'uranus':
        print(mass*8.9) 
        return mass*8.9
    if body == 'venus':
        print(mass*8.9) 
        return mass*8.9
    if body == 'mars':
        print(mass*3.7) 
        return mass*3.7
    if body == 'mercury':
        print(mass*3.7) 
        return mass*3.7
    if body == 'moon':
        print(mass*1.6) 
        return mass*1.6
    if body == 'pluto':
        print(mass*0.6) 
        return mass*0.6
    print('that could be anybody. Give mass and a major solar celestial body (lowercase) as arguments please')
    
# part 3 :
def pull(m1, m2, d):
    # G = 6.6743 * 10**-11 .... !=
    G = 6.674*10**-11
    print(G*((m1*m2)/d**2))
    return G*((m1*m2)/d**2)
    