# Imports
from tkinter import N
from typing import Any
import interface # file with the makeshift interface for super.py 
import file_manipulation # used to make, mutate and delete files and folders
import stock_manipulation # used to make, mutate and get informed on inventory
import date_manipulation # used to mutate and compare dates.
import argparse # Parser for command-line options, arguments and subcommands
import sys # used to further interface with the user

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

# when no arguments are provided in the command line, there will be a prompt to start the interface.
def start():
    interface.interface()

def main(): 
    print('')
    file_manipulation.dir_maker()  
    file_manipulation.time_file_maker()
    stock_manipulation.load_from_CSV_file()
    print('')
    guy = argparse.ArgumentParser()
    guy.add_argument('--list', action = 'store_true', help = 'Prints a list with the sellable stock available on the (current) set date.')
    guy.add_argument('--add', nargs=4, metavar=('-buy name-', '-quantity-', '-buy price-', '-expiration date-'), help='Adds an aquired item to the current stock. Requires 4 arguments: "product name", "quantity", "buy price" and "expiration date" (dd-mm-yyyy form).')
    guy.add_argument('--sell', nargs=3, metavar=('-sell name-', '-sell quantiy-', '-sell price-'), help='Sells an item from the current stock. Requires 3 arguments: "product name", "quantity sold" and "sell price"')
    arguments = guy.parse_args()
    if arguments.list == False\
    and type(arguments.add) == type(None)\
    and type(arguments.sell) == type(None):
        #if the command-line interface is not used, the program branches here 
        start()
    else:
        #if the command-line interface is used, the program branches here 
        if arguments.add:
            if len(arguments.add) == 4:
                try:
                    print('please make sure all arguments are correct, otherwise the save file might get corrupted.')
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
                    print('please make sure all arguments are correct, otherwise the save file might get corrupted.')
                    print(f'input is: name: {arguments.sell[0]}, quantity: {arguments.sell[1]}, price: {arguments.sell[2]}.')
                    print('continue?')
                    if interface.yes_or_no() == True:
                        print('')
                        stock_manipulation.selling_stock(arguments.sell[0], int(arguments.sell[1]), float(arguments.sell[2]))
                        print('\nif possible (no error messages above?), the product(s) are sold from stock\n')
                        stock_manipulation.overwrite_to_CSV_file()
                    else:
                        print('aborting')
                        sys.exit()
                except:
                    print('\n Failed selling the products')    
                    
# next is list, sales, etcetera
                
                
if __name__ == "__main__":
    main()
