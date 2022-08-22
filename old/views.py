import tkinter as tk
from tkinter import Button
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.constants import *


class View:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Correção de Provas - URBAM')
        self.root.geometry("1000x700")
        self.root.resizable(0, 0)
        # self.root.iconbitmap("img/icon.ico")
        self.frame = tk.Frame()
        self.tela1 = View.tela1(self)
        print("Init - Views")
        self.root.mainloop()

    def tela1(self):

        # Tela 1

        drop = ttk.Combobox(self.root, textvariable="",  state="readonly")
        drop.config(width=40)
        drop['values'] = ""
        drop.grid(column=0, row=1, sticky=W, padx=25, pady=10)
        # drop.current(0)
        # drop.bind("<<ComboboxSelected>>", self.controller.seleciona_ID)

        self.option = drop.bind()

        # Gera Botões

        # button_gerar_pasta = Button(text="Gerar Pasta", command=gera_pasta())
        button_gerar_pasta = Button(self.root, text="Gerar Pasta")
        button_gerar_pasta.grid(column=1, row=1, sticky=NW, padx=1, pady=20)
        button_gerar_pasta.configure(width=20)

        # button_gerar_gabarito = Button(self.root, text="Gerar Gabarito", command=lambda: open(self.inicia_gabarito()))
        button_gerar_gabarito = Button(text="Gerar Gabarito")
        button_gerar_gabarito.grid(column=2, row=1, padx=1, pady=20, sticky=N)
        button_gerar_gabarito.configure(width=20)

        # button_gerar_resultados = Button(text="Realizar Correção", command=self.controller.executa_correcao)
        button_gerar_resultados = Button(self.root, text="Realizar Correção")
        button_gerar_resultados.grid(column=3, row=1, padx=1, pady=20, sticky=N)
        button_gerar_resultados.configure(width=20)

        # button_exportar = Button(text="Exportar Dados", command=self.controller.salva_arquivo)
        button_exportar = Button(self.root, text="Exportar Dados")
        button_exportar.grid(column=4, row=1, padx=1, pady=20, sticky=N)
        button_exportar.configure(width=20)

        # Lista de todos os candidatos com notas e classificação (ainda não implementado por completo)

        text_lista_candidatos = scrolledtext.ScrolledText(self.root, width=117, height=40, state="disabled")
        text_lista_candidatos.grid(column=0, row=2, sticky=NSEW, padx=25, pady=5, columnspan=6)

    def tela2(self):
        pass
