import tkinter as tk
import os
from tkinter import ttk, scrolledtext


class View(tk.Tk):

    PAD = 10
    MAX_BUTTONS_PER_ROW = 5
    button_captions = ['Gerar Pasta', 'Gerar Gabarito', 'Realizar Correção', 'Exportar Dados']

    def __init__(self, controller):

        print("Init - View")

        super().__init__()

        self.value_var = tk.StringVar()

        self.controller = controller
        self.title("Correção de Concursos - URBAM")
        self.geometry("1000x700")
        self.resizable(0, 0)
        self.iconbitmap("img/icon.ico")

        self._make_main_frame()
        self._make_combo()
        self._make_scroll()
        self._make_buttons()
        self._center_window()

    def main(self):
        print("Main - View")
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_scroll(self):
        scroll = scrolledtext.ScrolledText(self, width=117, height=40, state="disabled")
        scroll.pack()

    def _make_buttons(self):
        self.outer_frm = ttk.Frame(self.main_frm)
        self.outer_frm.pack(padx=self.PAD, pady=self.PAD, side=tk.TOP)

        is_first_row = 'True'
        buttons_in_row = 0

        for caption in self.button_captions:  # Aqui estou criando os botões dinamicamente e dando pack nos mesmos
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:  # Aqui estou fazendo uma verificação pra poder colocar os quatro botões no máximo por linha

                is_first_row = False

                frm = ttk.Frame(self.outer_frm)
                frm.pack(fill='x')  # Aqui estou expandindo o botão 0

                buttons_in_row = 0

            btn = ttk.Button(frm, text=caption, command=(lambda button=caption: self.controller.on_button_click(button)), width=25)
            btn.pack(fill='x', expand=1, side='left')

    def _make_combo(self):

        drop = ttk.Combobox(self, textvariable="",  state="readonly")
        drop.config(width=40)
        drop['values'] = ""
        drop.pack(padx=self.PAD, pady=self.PAD, side=tk.TOP)

    def _make_path(self, path):

        self.isExist = os.path.exists(path)

        if not self.isExist:
            os.makedirs(path)
            tk.messagebox.showinfo(title='Correção de Provas - URBAM', message='Diretório criado com sucesso.')
            print("Diretório criado!")
        else:
            tk.messagebox.showwarning(title='Correção de Provas - URBAM', message='O diretório já existe.')
            print("Diretório já existe")

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
