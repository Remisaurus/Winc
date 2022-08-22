__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os

current_dir=os.path.join(os.getcwd(), 'files')
cache_dir=os.path.join(current_dir, 'cache')

#1
def clean_cache():
    if os.path.isdir(cache_dir):
        for all in os.listdir(cache_dir):
            os.remove(os.path.join(cache_dir, all))
        print("cache directory is present, and contents cleared")
    else:    
        os.mkdir(cache_dir)
        print("cache directory was absent, and new one created")

#2
import zipfile

def cache_zip(zip, dir):
    if zipfile.is_zipfile(zip):
        with zipfile.ZipFile(zip, mode="r") as archive:
            archive.extractall(dir)
    else:
        print(f'{zip} is not a zipfile')
    
#3
def cached_files():
    cached_files=[]
    for all in os.listdir(cache_dir):
        cached_files.append(os.path.join(cache_dir, all))
    return cached_files
  
#4
def find_password(filelist):
    indicator = 'password'
    for every in filelist:
        current_file = open(every, "r")
        for line in current_file:
            if indicator in line:
                print(f'{indicator} found in {every}')
                print(line)
                return line[10:].strip()
        current_file.close()