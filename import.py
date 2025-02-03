import os
from os import remove

file_name = "new_file.txt"

if os.path.exists(file_name):
    os.remove(file_name)