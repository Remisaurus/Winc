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

Even though I have learned my first PC steps on DOS in the nineties, I decided to make a slightly more user friendly interface than command lines for the program straight away. with the logic structure in place a command-line interface can be added later without too much trouble.
At first I thought the program should not just be able to set its date but also its time. However, since this ability would create needless complications (especially with over 24 hours offset and the interaction with setting the date) I decided to go forward without the ability to set the program's time. Most code that supported changing the time has been removed, but a few bits and pieces remain as you will no doubt see at some point.

There were no problems which I found really hard or could not solve by using my 'favourite' search engine. The biggest troubles I have had with this assignment were starting it and the amount of work I would have to put into it.
One of the things I found most difficult was testing with pytest. I started with testing the file_manipulator.py at the start, this did not seem to be hard. But when I started with input() I kind of left the pytest behind and started testing 'oldschool' with print() and breakpoint() statements.  


chapter 2,
in the course of,
As soon as I started the stock_manipulation file it hit me how hard this was going to be. problems were amassing faster than I could solve them and soon I needed paper to keep track of them. I decided to hold of the CSV for now and incorporate it later to store/retrieve information, and to go forward using tools I am familiar with like dictionaries. 
A problem that came up was that a check that I intend to perform will return only the first find it makes, while there might be multiple. the solution will be to first make a list of candidates from the whole population (thus all possibilities) and then perform the check on all items in that list. 
To test the functionality I went back to pytest, because it could be used fairly effectively and easily with the stock_manipulation file.
Purchase time(s) will now be a dictionary with howmany items were bought at a certain time if the same named product with same buy_price and expiry_date was aquired. Item's with that much similarity will recieve the same id.


Appendix
timeline:
29-08-2022 approximately 6 hours. 08:00 to 14:00
A file structure has been made as well as the code for file manipulation. a start has been made with the interface, and the date manipulation code. 
30-08-2022 approximatly 5 hours. 08:00 to 13:00
The interface and date manipulation are mostly finished today. file manipulation file has been expanded on.
31-08-2022 approximatly 7 hours 08:00 to 15:00
hardest day so far, layed a foundation in the stock manipulation file

