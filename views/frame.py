import tkinter as tk
from tkinter import ttk, scrolledtext
from views.alerts import WarningMixin, InfoMixin


class View(tk.Frame, WarningMixin, InfoMixin):

    PAD = 10
    MAX_BUTTONS_PER_ROW = 5

    def __init__(self, master=None):

        print("Init - View")

        super().__init__(master)

        self.value_var = tk.StringVar()

        self.buttons_captions_text = [
            "Gerar Pasta",
            "Gerar Gabarito",
            "Realizar Correção",
            "Exportar Dados",
        ]
        self.buttons= {}

        self._make_combo()
        self._make_scroll()
        self._make_buttons()
        self.pack()

    def _make_scroll(self):
        scroll = scrolledtext.ScrolledText(self, width=117, height=40, state="disabled")
        scroll.pack()

    def _make_buttons(self):

        is_first_row = "True"
        buttons_in_row = 0

        for (
            caption
        ) in (
            self.buttons_captions_text
        ):  # Aqui estou criando os botões dinamicamente e dando pack nos mesmos
            if (
                is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW
            ):  # Aqui estou fazendo uma verificação pra poder colocar os quatro botões no máximo por linha

                is_first_row = False

                frm = ttk.Frame(self)
                frm.pack(fill="x")  # Aqui estou expandindo o botão 0

                buttons_in_row = 0

            self.buttons[caption] = ttk.Button(
                frm,
                text=caption,
                width=25,
            )
            self.buttons[caption].pack(fill="x", expand=1, side="left")

    def _make_combo(self):

        drop = ttk.Combobox(self, textvariable="", state="readonly")
        drop.config(width=40)
        drop["values"] = ""
        drop.pack(padx=self.PAD, pady=self.PAD, side=tk.TOP)
