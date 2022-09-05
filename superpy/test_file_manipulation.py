import file_manipulation
import os

def test_CURRENT_DIR():
    assert file_manipulation.CURRENT_DIR == os.getcwd()
    
def test_dir_maker():
    file_manipulation.dir_maker()
    assert os.path.isdir(os.path.join(file_manipulation.CURRENT_DIR, 'data'))
    
def test_DATA_DIR():
    assert file_manipulation.DATA_DIR == os.path.join(file_manipulation.CURRENT_DIR, 'data')
    
def test_file_maker():
    file_manipulation.dir_maker()
    file_manipulation.file_maker()
    assert os.path.isfile(os.path.join(file_manipulation.DATA_DIR, 'current_stock.csv'))
    
def test_time_file_maker():
    file_manipulation.dir_maker()
    file_manipulation.time_file_maker()
    assert os.path.isfile(os.path.join(file_manipulation.DATA_DIR, 'set_date.txt'))