This file has been made to be used with a standard text editor.

Prefix
For Winc Academy I have been programming an assignment named SuperPy.
As the last requirement of this program assignment states:
“
Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose to implement it in this way. Include this in your repository as a report.md file.
•	You may use Markdown for your report, but it is not required.
•	To assist your explanation you may use code snippets.
“
This document has been made to fulfill that part of the SuperPy assignment.


chapter 1, 
Initially,

--0.1.0a-- Even though I have learned my first PC steps on DOS in the nineties, I decided to make a slightly more user friendly interface than command lines for the program straight away. with the logic structure in place, a command-line interface can be added later without too much trouble.
--0.1.0b-- At first I thought the program should not just be able to set its date but also its time. However, since this ability would create needless complications (especially with over 24 hours offset and the interaction with setting the date) I decided to go forward with only the ability to set the program's date and not time. Most code that supported changing the time has been removed, but a few bits and pieces remain as will no doubt be seen at some point.

There were no problems which I found really hard or could not solve by using my 'favourite' search engine. The biggest troubles I have had with this assignment so far were starting it and the amount of work I would have to put into it.
One of the things I found most difficult initially was testing with pytest. I did start with testing the file_manipulator.py, this did not seem to be hard. But when I started with input() I kind of left the pytest behind and started testing 'oldschool' with print() and breakpoint() statements.  


chapter 2,
in the course of,
--0.1.1a-- As soon as I started the stock_manipulation file it hit me how hard this was going to be. problems were amassing faster than I could solve them and soon I needed paper to keep track of them. I decided to hold of the CSV for now and incorporate it later to store/retrieve information, and to go forward using tools I am familiar with like dictionaries. 
A problem that came up was that a check that I intend to perform will return only the first find it makes, while there might be multiple. the solution will be to first make a list of candidates from the whole population (thus all possibilities) and then perform the check on all items in that list. 
To test the functionality I went back to pytest, because it could be used fairly effectively and easily with the stock_manipulation file.
Purchase time(s) will now be a dictionary with howmany items were bought at a certain time if the same named product with same buy_price and expiry_date was aquired. Item's with that much similarity will recieve the same id.
--0.1.1b-- A possibilty for adding stock is implemented that prompts for the data required.
For now, the interface is expanding at the fastest rate.
--0.1.1b2-- Expanded on the adding function. and the possibility to add quantity of items with near perfect similarity. adding new items with that much similarity will now add a buy date with quantity to a buydate dictionary.
problems fixed were not having () after function that should return value. and a function returning an integer was considered returning something True, since the function returns either True or a number a type check (type function()) == type(True) sufficed to fix the problem.
Further progress has produced a fairly complete add, remove and show current stock. The show current stock does not yet have its planned functionality, which will incorporate purchase/sell dates and amounts.
next CSV will be incorporated. 
--0.1.2a-- A function is made to write the main dictionary to a CSV file. ; has been chosen as the delimiter, and should therefore not be in any names.
--0.1.2b-- the thought was to write a function for loading the save file, but new problems became visible like loading a saved dictionary and saved time format strings, a solution for the time format saved string files was not too hard, but I did not manage to convert the dictionary-string saved back to a dictionary since it has keys in time format. A solution could be to change the dictionaries, but I have chosen to create an extra save file for the embedded dictionaries. 
A list (added as an appendix) has been created to state all the minor and big projects that still have to be done.
Further thinking produced a theory that it might have been easier to have the day by day changes in files, loading things up to a certain date only.
The plan is at the moment to check the whole dictionary to see which items are in stock at the set time, when information is asked the whole dictionary is checked again to fetch the required information. This method is far from efficient, changes may be made later on.
--0.1.2b2-- 
after a long struggle with how to save the embedded dictionary with variable length to CSV, it has been settled that the dateform items will be stored as strings and the whole dictionary as a string.

--0.2--
A big change is neccesary to get this to work. Everything I have now, I will save to an 'old' directory, some things I will be able to incorporate into a new version, but some things will not. 
The most desperate change neccesary is the embedded dictionary of variable length, it is very hard to save and load, from now on all the products aquired or sold will get their own id number. another big change will be the datetime objects which from now on will be properly stored as string values.

Appendix
To-do list (started 04-09-22, adittions are continually made since):
stars (*) mean the item has been done.

second save file, and function has to be coded for embedded dic. X decision X
load function should be made proper.
function to compare buy dates to set date should be made.
function to compare sell dates to set date should be made.
function to count total number of possible sales at set date should be made. 
function to create sales should be made. (including deducting them from stock at set time.)
show stock function has to be fixed to implement products not yet bought and are going to be bought.
show sales function (up till set date) should be made.
interface integration for command lines



Appendix
timeline:
29-08-2022 approximately 6 hours. 08:00 to 14:00
A file structure has been made as well as the code for file manipulation. a start has been made with the interface, and the date manipulation code. 
30-08-2022 approximatly 5 hours. 08:00 to 13:00
The interface and date manipulation are mostly finished today. file manipulation file has been expanded on.
31-08-2022 approximatly 7 hours 08:00 to 15:00
hardest day so far, layed a foundation in the stock manipulation file
01-09-2022 approximatly 4 hours 10:00 to 14:00
worked more on the interface and stock manipulation files. It is possible to add stock to an inner dictionary now.
02-09-2022 approximatly 7 hours 08:00 to 15:00
worked on stock manipulation and the interface to initiate it
03-09-2022 -> 05-09-2022 labour day longweekend in Canada
03-09-2022 approximatly 1 hour 
made a file manipulation function to write the main dictionary into a CSV file
04-09-2022 approximatly 1 hour
started on the function to load data and started to improve the save funtion
