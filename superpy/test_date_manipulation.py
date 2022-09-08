import file_manipulation
import stock_manipulation
import date_manipulation
import datetime
from file_manipulation import dir_maker
from file_manipulation import time_file_maker

dir_maker()
time_file_maker()

def test_get_date_datetime_form():
    assert type(date_manipulation.get_date_datetime_form(2222, 2, 22)) == type(datetime.datetime.now())
    
def test_types():
    assert type(date_manipulation.get_date_now_datetime_form()) == type(datetime.datetime.now())
    assert type(date_manipulation.get_date_set_datetime_form()) == type(datetime.datetime.now())
    assert type(date_manipulation.get_date_set()) == type('')
    assert type(date_manipulation.get_time_now()) == type('')
    assert type(date_manipulation.get_date_now()) == type('')
  
def test_earlier_check():
    # set date should not be absurdly high or low to test this function.
    assert date_manipulation.earlier_check('1-1-1000') 
    assert not date_manipulation.earlier_check('31-12-9999') 
    
def test_later_check():
    # set date should not be absurdly high or low to test this function.
    assert not date_manipulation.later_check('1-1-1000') 
    assert date_manipulation.later_check('31-12-9999') 
    
def test_compare_dates_greater():
    assert date_manipulation.compare_dates_greater(date_manipulation.get_date(2222, 2, 2), date_manipulation.get_date_now())
    
    