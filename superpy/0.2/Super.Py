# Imports
import interface # file with the makeshift interface for super.py 
import file_manipulation # used to make, mutate and delete files and folders
import stock_manipulation # used to make, mutate and get informed on inventory
import argparse # Parser for command-line options, arguments and subcommands
import sys # used to further interface with the user

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main(): 
    print('')
    file_manipulation.dir_maker()  
    file_manipulation.time_file_maker()
    stock_manipulation.load_from_CSV_file()
    print('')
    interface.interface()

if __name__ == "__main__":
    main()
