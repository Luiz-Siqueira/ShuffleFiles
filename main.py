import os
import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import interface

import re

def remove_number_hyphen(value):
    regex = r'\b\d+\s*-?\s*'
    
    val_whithout_number_with_hyphen = re.sub(regex, '', value)
    
    return val_whithout_number_with_hyphen

def alter_name_file():
    for file_name in os.listdir(folder):
        old_name = folder + file_name

        if ' - ' in file_name:
            file_name = remove_number_hyphen(file_name)

        indice_order = random.randint(0, 2**31 - 1)
        new_name = folder + str(indice_order) + ' - ' + file_name

        os.rename(old_name, new_name)


def alert_message():
    resultado = messagebox.askyesno("Alerta", "Ao reorganizar os arquivos de uma pasta, todos os arquivos do diretorio serão renomeados e esse processo é irreversivel! Deseja realizar esse processo?")
    if resultado:
        alter_name_file()
    



def open_dir():
    global folder
    diretorio = filedialog.askdirectory()

    if diretorio:
        interface.input_entry.config(state='normal')
        folder = diretorio + '/'
        interface.input_entry.insert(0, diretorio)

        print("Diretório selecionado:", diretorio)
        interface.input_entry.config(state='readonly')