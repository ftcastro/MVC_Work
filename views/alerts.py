import tkinter as tk


class WarningMixin:
    def showwarning(self, title, message):
        tk.messagebox.showwarning(title=title, message=message)

class InfoMixin:
    def showinfo(self, title, message):
        tk.messagebox.showinfo(title=title, message=message)
