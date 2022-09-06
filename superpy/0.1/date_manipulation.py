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
# provided arguments are valid. time will be defaulted at 00:00 (0 A.M. midnight)
def get_date_form(yyyy, mm, dd):
    return datetime.datetime.strptime(f'{yyyy}-{mm}-{dd}-0', '%Y-%m-%d-%H') 

# function to retrieve the date set within the program (returns string dd mm yyyy).
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
    
# function to check if argument date is earlier or same as the set date. Returns False if not
# date structure should be: datetime.datetime(yyyy, mm, dd)
def expired_check(date):
    if date <= get_date_set_datetime_form():
        return True
    elif date > get_date_set_datetime_form():
        return False
    
    
