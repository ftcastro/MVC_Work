"""Unused imports removed"""

from views.frame import View
from controllers.interface_controller import AbstractController


class Controller(AbstractController):
    def __init__(self):
        pass
    
    def bind(self,view, service):
        self.view = view
        self.service = service
        for k in self.view.buttons.keys():
            pass # TODO to configure buttons
    def consulta_area(self):
        self.service.consulta_area()
        print("Drop Current = ", self.view.tela1.drop.current())

        return self.lista_concursos

    def seleciona_id(
        self,
    ):
        self.options = self.view.telas.option
        result_id = self.service.seleciona_id(self.options)

    def gera_pasta(self):
        is_created, message = self.service.gera_pasta(
            path="H:/DIN/Fernando/concursos/teste"
        )

        if not is_created:
            self.view.showwarning(
                title="Correção de Provas - URBAM",
                message=message,
            )
        else:
            self.view.showinfo(
                title="Correção de Provas - URBAM",
                message=message,
            )

    def inicia_gabarito(self):
        print("Inicia Gabarito")

    def gera_gabarito(self):
        print("Gera Gabarito")

    def gravar_gabarito(self):
        print("Gravar Gabarito")

    def executa_correcao(self):
        print("Executa Correção")

    def salva_arquivo(self):
        print("Exporta Dados")
