import os
import sys
from turtle import clear
import file_manipulation
import date_manipulation
import stock_manipulation
import information
import calendar

# The code here is made for a makeshift interface that is slightly more user friendly than pure command-lines.
# The command line interface will be added however, since it is a prerequisite in the assignment.
# overall the contents of this file are not tested with pytest.

# function that prompts for pushing enter.
def push_enter():
    x = input('push enter')

# function that prompts for yes or no, returns True/False ((y/n)).
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

# function to clear the screen
def clearscreen():
    os.system('cls')

# Interface, prompts for interface start.    
def interface():
    print('start interface?')
    if yes_or_no() == True:
        clearscreen()
        main_question()
    else:
        sys.exit()

# function to input positive number or zero, returns positive integer or zero.    
def input_positive_number():
    this = input('positive number or 0: ')
    try:
        if int(this) >= 0:
            return int(this)
    except ValueError:
        if this == 'exit':
            # question has been integrated in the interface where the exit to stock_question should be possible.
            clearscreen()
            stock_question() 
        else:
            print('Input will need to be a whole number that is 0 or higher. Try again.')
            return input_positive_number()

# function to input year (between 1000 and 9999).    
def input_year():
    y = input('year (yyyy): ')
    try:
        if int(y) >= 1000 and int(y) <= 9999:
            return int(y)
        else:
            print('Invalid year number (valid numbers: 1000-9999), try again.')
            return input_year()
    except ValueError:
        print('Try again. Please input a number between 1000 and 9999.')
        return input_year()

# function to input month.       
def input_month():
    m = input('month (mm): ')
    try:
        if int(m) >= 1 and int(m) <= 12:
            return int(m) 
        else:
            print('Invalid month number, there are 12 months in a year. try again')
            return input_month()
    except ValueError:
        print('Invalid input, try again please. Monthnumbers are 1-12')
        return input_month()

# function to input day given year and month. 
def input_day(y, m):
    d = input('day (dd): ')
    try:
        if int(d) >= 1 and int(d) <= calendar._monthlen(y, m):
            return int(d) 
        else:
            print(f'there are {calendar._monthlen(y, m)} days in that particular month and year. Try again.')
            return input_day(y, m)
    except ValueError:
        print('Invalid input, try again with a number please.')
        return input_day(y, m)

# Interface, prompts for what action is wanted and redirects there. 
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
        # save here
        sys.exit()
    elif x == 'exit':
        # save here
        sys.exit()
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

# Interface, prompts and runs reset function if desired.
def reset_question():
    print('This reset will delete all files in the data folder.')
    print('Are you sure?')
    if yes_or_no() == True:
        file_manipulation.reset_data()
        print('')
        print('go back to main screen?')
        if yes_or_no() == True:
            clearscreen()
            main_question()
        else:
            quit
    else:
        clearscreen()
        main_question()
        
# Interface, prompts for what action is wanted and redirects there.                 
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

# Interface, prompts for what action is wanted and redirects there.        
def stock_question():
    print('Stock related business')
    print('') 
    print('Type \'stock\' to see the current inventory, \'add\' to add to the stock or \'rem\' to remove from the stock.')
    print('Type \'back\' to go back. (Important, answers without capitals)')
    x = input('')
    if x == 'stock':
        clearscreen()
        stock_manipulation.print_current_stock()
        push_enter()
        clearscreen()
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

# Interface, prompts for which information would like to be seen and makes a function print it.  
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
        push_enter()
        clearscreen()
        info_question()
    elif x == 'help':
        clearscreen()
        information.print_interface_help()
        push_enter()
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
        
# Interface, prompts for number, will initiate function to write this number to a text file.
# This number will be the days offset for program's set time.
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
            file_manipulation.set_date(int(x))
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
            print('Invalid input received. Try again.')
            print('')
            set_question()
            
# Interface, prompts for number, will initiate adding_question with that number   
def add_question():
    print('Adding stock')
    print('') 
    print('Howmany differently named items would you like to add? (positive whole number required)')
    print('Type \'back\' to go back. (without capitals)')
    x = input('')
    try:
        if int(x) > 0:
            clearscreen()
            adding_question(int(x))
            clearscreen()
            stock_question()    
    except ValueError:
        if x == 'back':
            clearscreen()
            stock_question()
        else:
            print('')
            print('Please follow the input rules.')
            print('')
            add_question()

# Interface, prompts for name, it will remove all items with the same name from the stock (not same as selling)
def rem_question():
    print('Removing stock')
    print('') 
    print('Howmany differently named items would you like to remove? (positive whole number required)')
    print('Type \'back\' to go back. (without capitals)')
    x = input('')
    try:
        if int(x) > 0:
            clearscreen()
            removing_question(int(x))
            clearscreen()
            stock_question()
    except ValueError:
        if x == 'back':
            clearscreen()
            stock_question()
        else:
            print('')
            print('That input will not do. Try again.')
            print('')
            rem_question()
            
# function which will prompt questions about items before adding those items to the stock    
def adding_question(number):
    for all in range(number+1):
        if all == 0:
            continue 
        print(f'product number {all}')
        def get_name():
            print('product\'s name? (type exit to stop adding products) (; is reserved)')
            a = input('name: ')
            if a == 'exit':
                clearscreen()
                stock_question()
            if ';' in a:
                clearscreen()
                print('')
                print('You cannot add a name with a \';\' in it')
                print('try again')
                print('')
                return get_name()
            else:
                return a
        a = get_name()
        print('quantity? (type exit to stop adding products)')
        b = input_positive_number()
        if b == 'exit':
            clearscreen()
            stock_question()
        print('price at which the product was aquired? (type exit to stop adding products)')
        c = input_positive_number()
        if c == 'exit':
            clearscreen()
            stock_question()
        print('product\'s expiry date? (31-12-9999 = example for none)')
        y = input_year()
        m = input_month()
        d = input_day(y, m)
        stock_manipulation.add_stock(a, b, c, date_manipulation.get_date_form(y, m, d).strftime("%d-%m-%Y"))
        print('added to stock.')
        push_enter()
        clearscreen()
        
# function which will prompt question about items before removing them from the stock          
def removing_question(number):
    for all in range(number+1):
        if all == 0:
            continue 
        print(f'product number {all}')
        print('product\'s name? (type exit to stop removing products)')
        print('keep in mind this will remove ALL instances with the EXACT input name from the stock')
        print('this action is not the same as setting stock to a sold status)')
        a = input('name: ')
        if a == 'exit':
            clearscreen()
            stock_question()
        else:
            if stock_manipulation.product_exists(a) == False:
                print('')
                print('No item by that name found in stock.')
                push_enter()
                clearscreen()
            else:
                print ('')
                print (f'This will remove ALL instances with the name:\'{a}\' from the stock')
                print ('are you sure?')
                if yes_or_no() == True:
                    stock_manipulation.removing_stock(a)
                    print('')
                    print(f'item(s) with the name:\'{a}\' removed from stock')
                    push_enter()
                    clearscreen()
                else:
                    print('')
                    print('Aborting')
                    push_enter()
                    clearscreen()
                    break
                
                
file_manipulation.file_maker()         
stock_manipulation.load_from_CSV_file()
print(date_manipulation.get_date_form(1111, 1, 1))
stock_manipulation.products[1] = stock_manipulation.product(1, 'test', 44, 5, 'now', date_manipulation.get_date_form(1111,11,11), False)
stock_manipulation.add_stock('test', 100, 5, date_manipulation.get_date_form(1111, 11, 11))            
stock_manipulation.add_stock('remi', 5, 100, date_manipulation.get_date_form(1111, 11, 11))
stock_manipulation.add_stock('kara', 1, '100000', date_manipulation.get_date_form(1111, 11, 11))
stock_manipulation.add_stock('remi', 7, 100, date_manipulation.get_date_form(1111, 11, 11))                
               


#stock_manipulation.overwrite_to_CSV_file()
stock_manipulation.print_current_stock()    


stock_manipulation.overwrite_to_CSV_file()