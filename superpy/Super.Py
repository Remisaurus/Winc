# Imports
import interface # file with the makeshift interface for super.py 
import file_manipulation # used to make, mutate and delete files and folders
import stock_manipulation # used to make, mutate and get informed on inventory
import date_manipulation # used to mutate and compare dates.
import argparse # Parser for command-line options, arguments and subcommands
import sys 

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

# This is the main file and the program is started from here. 
# However, this file merely houses the code for the command-line interface. 
# most of the code can be found in the other files.
# overall the contents of this file are not tested with 'pytest'.

# when no arguments are provided in the command line, there will be a prompt to start the built-in interface.
def start():
    interface.interface()

# the main 'switch' for the code. contains the command-line interface.
def main(): 
    print('')
    file_manipulation.dir_maker()  
    file_manipulation.time_file_maker()
    stock_manipulation.load_from_CSV_file()
    print('')
    guy = argparse.ArgumentParser()
    guy.add_argument('--start', action = 'store_true', help = 'starts the interface from which all can be controlled more simply. Same is achieved by starting the program without command lines.')
    guy.add_argument('--list', action = 'store_true', help = 'Prints a list with the sellable stock available on the (current) set date.')
    guy.add_argument('--add', nargs=4, metavar=('-buy name-', '-quantity-', '-buy price-', '-expiration date-'), help='Adds an aquired item to the current stock. Requires 4 arguments: "product name", "quantity", "buy price" and "expiration date" (dd-mm-yyyy form).')
    guy.add_argument('--sell', nargs=3, metavar=('-sell name-', '-sell quantiy-', '-sell price-'), help='Sells an item from the current stock. Requires 3 arguments: "product name", "quantity sold" and "sell price"')
    guy.add_argument('--settime', type = int, metavar=('-days-'), help = 'The argument sets the program\'s time that many days from the current system time. (input minus (-) for past, and 0 to set back to system time)')
    guy.add_argument('--sales', metavar=('-date-'), help = 'Will show you the sales on the argument date (dd-mm-yyyy form)')
    guy.add_argument('--salesuntill', metavar=('-date-'), help = 'Will show you the sales up to and including the argument date (dd-mm-yyyy form)')
    guy.add_argument('--salest', action = 'store_true', help = 'Will show you the sales on the program\'s set date')
    guy.add_argument('--salesuntillt', action = 'store_true', help = 'Will show you the sales up to and including the program\'s set date')
    guy.add_argument('--remove', type = str, metavar=('-product name-'), help = 'completely removes all the products with the argument\'s name from the stock (sold, bought and expired).' )
    guy.add_argument('--reset', action = 'store_true', help = 'Will completely reset all data and reinstate clean stock and time files.')
    guy.add_argument('--listexp', metavar=('-date-'), help = 'lists expired items up to and including on the argument date (dd-mm-yyyy form)')
    guy.add_argument('--listexpt', action = 'store_true', help = 'lists expired items up to and including on the program\'s set date')
    arguments = guy.parse_args()
    if arguments.list == False\
    and arguments.start == False\
    and arguments.reset == False\
    and arguments.salest == False\
    and arguments.salesuntillt == False\
    and arguments.listexpt == False\
    and type(arguments.listexp) == type(None)\
    and type(arguments.remove) == type(None)\
    and type(arguments.add) == type(None)\
    and type(arguments.settime) == type(None)\
    and type(arguments.sell) == type(None)\
    and type(arguments.sales) == type(None)\
    and type(arguments.salesuntill) == type(None):
        #if the command-line interface is not used, the program branches here 
        start()
    else:
        #if the command-line interface is used, the program branches here 
        if arguments.start:
            start()
            sys.exit()
        if arguments.reset:
            print('this reset will remove all saved data and files from the data directory, are you sure?')
            if interface.yes_or_no():
                file_manipulation.reset_data()
            else:
                print('aborting')
                sys.exit()
        if arguments.settime != None: # could be 0. 
             file_manipulation.set_date(arguments.settime)
             print(f'date set to {arguments.settime} days from system\'s time')
        if arguments.remove != None:
            print(f'removing all instances with the name :\'{arguments.remove}\' from the stock.')
            print('Are you sure?')
            if interface.yes_or_no():
                stock_manipulation.removing_stock(arguments.remove)
                stock_manipulation.overwrite_to_CSV_file()
            else:
                print('aborting')
                sys.exit()
        if arguments.add:
            if len(arguments.add) == 4:
                try:
                    print('please make sure all arguments are correct, otherwise the save file might get corrupted and not load the added data.')
                    print(f'input is: name: {arguments.add[0]}, quantity: {arguments.add[1]}, price: {arguments.add[2]}, date of expiry (form dd-mm-yyyy): {arguments.add[3]}.')
                    print('continue?')
                    if interface.yes_or_no() == True:
                        stock_manipulation.add_stock(arguments.add[0], arguments.add[1], arguments.add[2], arguments.add[3])
                        print('product added')
                        stock_manipulation.overwrite_to_CSV_file()
                    else:
                        print('aborting')
                        sys.exit()
                except:
                    print('\n failed to add product.')
        if arguments.sell:
            if len(arguments.sell) == 3:
                try:
                    print('please make sure all arguments are correct, otherwise errors might occur.')
                    print(f'input is: name: {arguments.sell[0]}, quantity: {arguments.sell[1]}, price: {arguments.sell[2]}.')
                    check = stock_manipulation.sellable_stock(arguments.sell[0])
                    print(f'there are {check} items of {arguments.sell[0]} available for sale in stock')
                    print('continue?')
                    if interface.yes_or_no() == True:
                        print('')
                        stock_manipulation.selling_stock(arguments.sell[0], int(arguments.sell[1]), float(arguments.sell[2]))
                        print('\nIf there are no error messages above, the product(s) are sold from stock\n')
                        stock_manipulation.overwrite_to_CSV_file()
                    else:
                        print('aborting')
                        sys.exit()
                except:
                    print('\n Failed selling the products')   
        if arguments.list:
            stock_manipulation.print_current_stock()
        if arguments.sales:
            stock_manipulation.sales_set_date(arguments.sales)
        if arguments.salesuntill:
            try:
                stock_manipulation.sales_till_date(arguments.salesuntill)
            except:
                print('\nAn error has occured. please input the correct format of dd-mm-yyyy.\n')
        if arguments.salest:
             stock_manipulation.sales_set_date(date_manipulation.get_date_set())
        if arguments.salesuntillt:
            stock_manipulation.sales_till_date(date_manipulation.get_date_set())
        if arguments.listexp:
            try:
                stock_manipulation.get_expired_items(arguments.listexp)
            except:
                print('\nAn error has occured. please input the correct format of dd-mm-yyyy.\n')
        if arguments.listexpt:
            stock_manipulation.print_expired_items()

# only if the program is ran locally it will execute main.               
if __name__ == "__main__":
    main()
