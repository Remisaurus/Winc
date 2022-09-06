import date_manipulation
import datetime
import file_manipulation

file_manipulation.dir_maker()
file_manipulation.time_file_maker()

def test_get_date_form():
    assert type(date_manipulation.get_date_form(2222, 2, 22)) == type(datetime.datetime.now())
    
def test_types():
    assert type(date_manipulation.get_date_now_datetime_form()) == type(datetime.datetime.now())
    assert type(date_manipulation.get_date_set_datetime_form()) == type(datetime.datetime.now())
    assert type(date_manipulation.get_date_set()) == type('')
    assert type(date_manipulation.get_time_now()) == type('')
    assert type(date_manipulation.get_date_now()) == type('')
  
def test_expired_check():
    # set date should not be absurdly high or low to test this function.
    assert date_manipulation.expired_check(date_manipulation.get_date_form(1000, 1, 1)) 
    assert not date_manipulation.expired_check(date_manipulation.get_date_form(9999, 12, 31)) 
    
    