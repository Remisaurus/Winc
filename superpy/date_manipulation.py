import datetime
import file_manipulation

# function to get the current time in string form.
def get_time_now():
    return datetime.datetime.now().strftime("%H:%M:%S")

# function to get current date in string form.
def get_date_now():
    return datetime.datetime.now().strftime("%d-%m-%Y")

# function to get current date in datetime object form.
def get_date_now_datetime_form(): 
    return datetime.datetime.now()

# rudimentary function. defaulted to be the same as get time now, kept to keep functionality in the program.
def get_time_set():
    return get_time_now()

# function to return a datetime object from year, month and day.
# provided arguments are valid, time will be defaulted at 00:00 (0 A.M. midnight)
def get_date_datetime_form(yyyy, mm, dd):
    return datetime.datetime.strptime(f'{yyyy}-{mm}-{dd}-0', '%Y-%m-%d-%H')

# function to return a standard string from year, month and day.
# provided arguments are valid, time will be defaulted at 00:00 (0 A.M. midnight)
def get_date(yyyy, mm, dd):
    return datetime.datetime.strptime(f'{yyyy}-{mm}-{dd}-0', '%Y-%m-%d-%H').strftime("%d-%m-%Y")  

# function to retrieve the date set within the program (returns standard string dd mm yyyy).
def get_date_set():
    file_manipulation.time_file_maker()
    with open(file_manipulation.SET_DATE_FILE, 'r') as boss:
        change_date = boss.readline()
        if change_date == 'now':
            days_to_change = 0
        else:
            try:
                days_to_change = int(change_date)
            except ValueError:
                print('The program\'s date file is corrupted.')
                print('Perform a reset or manually delete the file from the data dir and restart the program.')
                print('Defaulting to system time.')
                days_to_change = 0
    return (datetime.datetime.now() + datetime.timedelta(days = days_to_change)).strftime("%d-%m-%Y")

# function to retrieve the date set within the program (returns datetime object).
def get_date_set_datetime_form():
    with open(file_manipulation.SET_DATE_FILE, 'r')as boss:
        change_date = boss.readline()
        if change_date == 'now':
            days_to_change = 0
        else:
            try:
                days_to_change = int(change_date)
            except ValueError:
                print('The program\'s date file is corrupted.')
                print('Perform a reset or manually delete the file from the data dir and restart the program.')
                print('Defaulting to system time.')
                days_to_change = 0
    return (datetime.datetime.now() + datetime.timedelta(days = days_to_change))
    
# function to check if argument date is earlier or same as the set date. Returns False if not (standard string input)
def earlier_check(date):
    dateform = datetime.datetime.strptime(date, '%d-%m-%Y')
    return dateform <= get_date_set_datetime_form()
    
# function to check if first argument date is earlier or same as the second date. Returns False if not (standard string input)
def earlier_than(date1, date2):
    dateform1 = datetime.datetime.strptime(date1, '%d-%m-%Y')
    dateform2 = datetime.datetime.strptime(date2, '%d-%m-%Y')
    return dateform1 <= dateform2
    
# function to check if argument date is later or same as the set date. Returns False if not (standard string input)
def later_check(date):
    dateform = datetime.datetime.strptime(date, '%d-%m-%Y')
    return dateform >= get_date_set_datetime_form()
    
# returns datetime object from standard string used by this code
def get_string_in_date_form(date):
   return datetime.datetime.strptime(date, '%d-%m-%Y')

# returns result after comparing date(time objects)s with >= (used in selling function)
def compare_dates(date1, date2):
    return date1 >= date2

# returns result of comparing string dates with > (used in getting sales up to and including function)
def compare_dates_greater(date1, date2):
    a = datetime.datetime.strptime(date1, '%d-%m-%Y')
    b = datetime.datetime.strptime(date2, '%d-%m-%Y')
    return a > b
