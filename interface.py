from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from main import open_dir
from main import alert_message

janela = Tk()
janela.title("ShuffleFiles")

caminho_icone = 'icon.ico'
janela.iconbitmap(caminho_icone)


text_orientacao = Label(janela, text="Escolha um diretorio onde os arquivos se encontram").grid(column=0, row=0, padx=10, pady=10)
frame = Frame(janela)
frame.grid(row=1, column=0, padx=10, pady=10)


input_entry = Entry(frame, font=30)
input_entry.grid(row=0, column=0, padx=0)
input_entry.config(state='readonly')

open_dir_button = Button(frame, text="Buscar diretorio", command=open_dir).grid(row=0, column=1, padx=0)
reorder_button = Button(janela, text="Reordenar arquivos", command=alert_message).grid(row=3, column=0, padx=10, pady=10)


janela.mainloop()