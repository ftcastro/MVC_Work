import tkinter as tk
import os
from tkinter import ttk, scrolledtext
from views.alerts import WarningMixin, InfoMixin


class View(tk.Tk, WarningMixin, InfoMixin):

    PAD = 10
    MAX_BUTTONS_PER_ROW = 5

    def __init__(
        self,
    ):

        print("Init - View")

        super().__init__()

        self.value_var = tk.StringVar()
        self.title("Correção de Concursos - URBAM")
        self.geometry("1000x700")
        self.resizable(0, 0)
        self.iconbitmap("img/icon.ico")
        self.buttons_captions_text = [
            "Gerar Pasta",
            "Gerar Gabarito",
            "Realizar Correção",
            "Exportar Dados",
        ]
        self.button_captions = {""}

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

        is_first_row = "True"
        buttons_in_row = 0

        for (
            caption
        ) in (
            self.button_captions
        ):  # Aqui estou criando os botões dinamicamente e dando pack nos mesmos
            if (
                is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW
            ):  # Aqui estou fazendo uma verificação pra poder colocar os quatro botões no máximo por linha

                is_first_row = False

                frm = ttk.Frame(self.outer_frm)
                frm.pack(fill="x")  # Aqui estou expandindo o botão 0

                buttons_in_row = 0

            self.button_captions[caption] = ttk.Button(
                frm,
                text=caption,
                width=25,
            )
            self.button_captions[caption].pack(fill="x", expand=1, side="left")

    def _make_combo(self):

        drop = ttk.Combobox(self, textvariable="", state="readonly")
        drop.config(width=40)
        drop["values"] = ""
        drop.pack(padx=self.PAD, pady=self.PAD, side=tk.TOP)

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
