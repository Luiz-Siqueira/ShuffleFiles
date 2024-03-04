import os
import random
from tkinter import *
from tkinter import filedialog


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


def open_dir():
    global folder
    diretorio = filedialog.askdirectory()
    if diretorio:
        input_entry.config(state='normal')
        folder = diretorio + '/'
        input_entry.insert(0, diretorio)

        print("Diretório selecionado:", diretorio)
        input_entry.config(state='readonly')


janela = Tk()
janela.title("ShuffleFiles")

text_orientacao = Label(janela, text="Escolha um diretorio onde os arquivos se encontram").grid(column=0, row=0, padx=10, pady=10)
frame = Frame(janela)
frame.grid(row=1, column=0, padx=10, pady=10)


input_entry = Entry(frame, font=30)
input_entry.grid(row=0, column=0, padx=0)
input_entry.config(state='readonly')

open_dir_button = Button(frame, text="Buscar diretorio", command=open_dir).grid(row=0, column=1, padx=0)
reorder_button = Button(janela, text="Reordenar arquivos", command=alter_name_file).grid(row=3, column=0, padx=10, pady=10)


janela.mainloop()


