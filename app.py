"""The entry point was fixed with the correct class names"""
import tkinter as tk
from controllers.domain_controller import Controller
from models.model import Model
from views.frame import View
from services.your_service import DomaineService


class Application(tk.Tk):
    def __init(self):
        self.master = super().__init__()

    def attach(self, controller, view, service):
        view = view(self.master)
        controller.bind(view, service)


if __name__ == "__main__":
    view = View
    model = Model
    service = DomaineService(model)
    controller = Controller()
    app = Application()
    app.attach(view=view, service=service, controller=controller)
    app.mainloop()
