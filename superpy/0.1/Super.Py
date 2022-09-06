# Imports
import interface # file with the makeshift interface for super.py 
import file_manipulation # used to make,mutate and delete files and folders
import argparse # Parser for command-line options, arguments and subcommands
import sys # used to further interface with the user
import csv # comma seperated values (major in spreadsheets and databases)

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main(): 
    print('')
    file_manipulation.dir_maker()  
    file_manipulation.file_maker()
    file_manipulation.time_file_maker()
    print('')
    interface.interface()
'''
here are three command-line fundamentals you should search the web for before you dive into the exercise:

stdin
stdout
command-line arguments
The argparse module helps you to write your own command-line tool. Now that you know about command-line arguments, you should be able to see why it's named argparse.
'''
'''
SuperPy
A large supermarket chain has asked you to write a command-line tool that is able to keep track of their inventory: they want to call it SuperPy. The core functionality is about keeping track and producing reports on various kinds of data:

Which products the supermarket offers;
How many of each type of product the supermarket holds currently;
How much each product was bought for, and what its expiry date is;
How much each product was sold for or if it expired, the fact that it did;
All data must be saved in CSV files. Feel free to come up with your own file structure,
but here's an example structure to get started with if you want:

Filename        Columns
bought.csv      id,product_name,buy_date,buy_price,expiration_date
sold.csv        id,bought_id,sell_date,sell_price
Note

In this example structure, the id column is an integer that is incremented for each line.
This allows for some clever matching of items between different tables.
You will later see this pattern a lot in databases, where it is particularly powerful.
'''
'''
Your program should have an internal conception of what day it is -- perhaps saved to a simple text file -- that we can advance time by two days by using a command like:

$ python super.py --advance-time 2
'''
'''
Interaction with your program must go through the command-line.
Here's an example of what a sequence of interactions could look like:

$ python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01
OK

$ python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+

$ python super.py --advance-time 2
OK

$ python super.py report inventory --yesterday
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange       | 1     | 0.8       | 2020-01-01      |
+--------------+-------+-----------+-----------------+

$ python super.py sell --product-name orange --price 2
OK

$ python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+


$ python super.py report revenue --yesterday
Yesterday's revenue: 0

$ python super.py report revenue --today
Today's revenue so far: 2

$ python super.py report revenue --date 2019-12
Revenue from December 2019: 0

$ python super.py report profit --today
1.2

$ python super.py sell --product-name orange --price 2
ERROR: Product not in stock.
'''
'''
Code
Be creative with your implementation! We intentionally keep the specification open to encourage you to be creative with this project.
However, to obtain a passing grade, you will at least need to satisfy the following requirements:

Well-structured and documented code, including:
Clear and effective variable and function names;
Use of comments where the code does not speak for itself;
Clear and effective separation of code into separate functions and possibly files.
Use of modules to the extent that it shows you were able to independently read and understand the documentation,
and apply the techniques within:
csv
*argparse*
datetime, including in particular the date object, strftime
and *strptime* functions and datetime arithmetic using timedelta.

Use of external text files (CSV) to read and write data.
*A well-structured and user friendly command-line interface with -
- clear descriptions of each argument in the --help section.
*A text file containing a usage guide aimed with peers as the target audience. -
- The usage guide should include plenty of examples.*

The application must support:
Setting and advancing the date that the application perceives as 'today';
*Recording the buying and selling of products on certain dates;
*Reporting revenue and profit over specified time periods;
*Exporting selections of data to CSV files;
Two other additional non-trivial features of your choice, for example:
The use of an external module Rich to improve the application.
The ability to import/export reports from/to formats other than CSV (in addition to CSV)
The ability to visualize some statistics using Matplotlib
Another feature that you thought of.
'''
'''
Report
Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose to implement it in this way. Include this in your repository as a report.md file.

You may use Markdown for your report, but it is not required.
To assist your explanation you may use code snippets.
'''


if __name__ == "__main__":
    main()
