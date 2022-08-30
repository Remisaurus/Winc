import datetime
import file_manipulation

def get_time_now():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date_now():
    return datetime.datetime.now().strftime("%d-%m-%Y")

def get_time_set():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date_set():
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
    return (datetime.datetime.now() + datetime.timedelta(days = days_to_change)).strftime("%d-%m-%Y")

