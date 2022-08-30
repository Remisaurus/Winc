import os
import file_manipulation
import date_manipulation
import information

# The code here is made for a makeshift interface that is slightly more user friendly than pure command-lines.
# The command line interface will be added however since it is a prerequisite in the assignment.

def yes_or_no():
    print('yes or no')
    x = input('')
    if x == 'y':
        return True
    elif x == 'yes':
        return True
    elif x == 'Y':
        return True
    elif x == 'Yes':
        return True
    elif x == 'YES':
        return True
    elif x == 'n':
        return False
    elif x == 'no':
        return False
    elif x == 'N':
        return False
    elif x == 'No':
        return False
    elif x == 'NO':
        return False
    else:
        print('respond with Yes or No please. (y or n is also accepted)')
        return yes_or_no()

def clearscreen():
    os.system('cls')
        
def main_question():
    print('Super.Py')
    print('')
    print(f'System time: {date_manipulation.get_time_now()} on date: {date_manipulation.get_date_now()}')
    print(f"Program's set time: {date_manipulation.get_time_set()} on date: {date_manipulation.get_date_set()}")
    print('')
    print('What is your business?')
    print('Type \'time\' for setting time, \'stock\' for inventory related business or \'info\' for additional information.')
    print('Type \'quit\' or \'exit\' to terminate the program. Type \'reset\' to reset all data. (Important, all answers without capitals)')
    x = input('')
    if x == 'quit':
        quit
    elif x == 'exit':
        quit
    elif x == 'time':
        clearscreen()
        time_question()
    elif x == 'info':
        clearscreen()
        info_question()
    elif x == 'stock':
        clearscreen()
        stock_question()
    elif x == 'reset':
        clearscreen()
        reset_question()
    else:
        print('') 
        print('Faulty input. Try again:')
        print('') 
        main_question()

def reset_question():
    print('This reset will delete all files in the data folder.')
    print('Are you sure? (y/n)')
    if yes_or_no() == True:
        file_manipulation.reset_data()
        print('')
        print('go back to main screen? (y/n)')
        if yes_or_no() == True:
            clearscreen()
            main_question()
        else:
            quit
    else:
        clearscreen()
        main_question()
                
def time_question():
    print('Time related business')
    print('') 
    print(f'System time: {date_manipulation.get_time_now()} on date: {date_manipulation.get_date_now()}')
    print(f"Program's set time: {date_manipulation.get_time_set()} on date: {date_manipulation.get_date_set()}")
    print('') 
    print('Type \'set\' to set, or \'reset\' to reset the programs time. Type \'back\' to go back.')
    print('all answers without capitals)')
    x = input('')
    if x == 'set':
        clearscreen()
        set_question()
    elif x == 'reset':
        file_manipulation.reset_time()
        clearscreen()
        print('Set time has been reset to system time.')
        print('')
        time_question()
    elif x == 'back':
        clearscreen()
        main_question()
    else:
        print('')
        print('Invalid input, please try again.')
        print('')
        time_question()
        
def stock_question():
    print('Stock related business')
    print('') 
    print('Type \'stock\' to see the current inventory, \'add\' to add to the stock or \'rem\' to remove from the stock.')
    print('Type \'back\' to go back. (Important, answers without capitals)')
    x = input('')
    if x == 'stock':
        clearscreen()
        print('function not implemented yet')
        stock_question()
    elif x == 'add':
        clearscreen()
        add_question()
    elif x == 'rem':
        clearscreen()
        rem_question()
    elif x == 'back':
        clearscreen()
        main_question()
    else:
        print('')
        print('That is not a valid input, try again.')
        print('')
        stock_question()
        
def info_question():
    print('Information')
    print('') 
    print(f'System time: {date_manipulation.get_time_now()} on date: {date_manipulation.get_date_now()}')
    print(f"Program's set time: {date_manipulation.get_time_set()} on date: {date_manipulation.get_date_set()}")
    print('') 
    print('Type \'ass\' to read the assignment this program has been build for, type \'help\' to read how to use the program.')
    print('Type \'back\' to go back. (all answers without capitals)')
    x = input('')
    if x == 'ass':
        clearscreen()
        information.print_assignment()
        print('ready to go back? (y/n) (no will quit)')
        if yes_or_no() == True:
            clearscreen()
            info_question()
        else:
            quit
    elif x == 'help':
        clearscreen()
        information.print_interface_help()
        print('ready to go back? (y/n) (no will quit)')
        if yes_or_no() == True:
            clearscreen()
            info_question()
    elif x == 'back':
        clearscreen()
        main_question()
    else:
        print('')
        print('Invalid input, please try again.')
        print('')
        time_question()
        
def set_question():
    print('Setting the program\'s date')
    print('') 
    print(f'System time: {date_manipulation.get_time_now()} on date: {date_manipulation.get_date_now()}')
    print(f"Program's set time: {date_manipulation.get_time_set()} on date: {date_manipulation.get_date_set()}")
    print('') 
    print('Howmany days from the current date do you wish the program\'s set date to be?')
    print('Only whole numbers are accepted. Negative values set the date to the past.')
    print('Type \'back\' to go back. (without capitals)')
    x = input('')
    try:
        if type(int(x)) == type(1):
            file_manipulation.set_date(x)
            clearscreen()
            print(f'Date set with {int(x)} days as offset')
            print('')
            time_question()
    except ValueError:
        if x == 'back':
            clearscreen()
            time_question()
        else:
            print('')
            print('invalid input received. Try again.')
            print('')
            set_question()
        
def add_question():
    print('Adding stock')
    print('') 
    print('Howmany differently named items would you like to add? (positive whole number required)')
    print('Type \'back\' to go back. (without capitals)')
    x = input('')
    try:
        if int(x) > 0:
            clearscreen()
            print('function not implemented yet')
            add_question()
    except ValueError:
        if x == 'back':
            clearscreen()
            stock_question()
        else:
            print('')
            print('Please follow the input rules.')
            print('')
            add_question()

def rem_question():
    print('Removing stock')
    print('') 
    print('Howmany differently named items would you like to remove? (positive whole number required)')
    print('Type \'back\' to go back. (without capitals)')
    x = input('')
    try:
        if int(x) > 0:
            clearscreen()
            print('function not implemented yet')
            add_question()
    except ValueError:
        if x == 'back':
            clearscreen()
            stock_question()
        else:
            print('')
            print('That input will not do. Try again.')
            print('')
            add_question()
     
def interface():
    print('start interface?')
    if yes_or_no() == True:
        clearscreen()
        main_question()
    else:
        quit