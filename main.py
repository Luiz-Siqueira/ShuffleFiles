import os
import random

folder = r'E:\\'

import re

def remove_number_hyphen(value):
    regex = r'\b\d+\s*-?\s*'
    
    val_whithout_number_with_hyphen = re.sub(regex, '', value)
    
    return val_whithout_number_with_hyphen

for file_name in os.listdir(folder):
    old_name = folder + file_name

    if ' - ' in file_name:
        file_name = remove_number_hyphen(file_name)

    indice_order = random.randint(0, 2**31 - 1)
    new_name = folder + str(indice_order) + ' - ' + file_name

    os.rename(old_name, new_name)


print(os.listdir(folder))