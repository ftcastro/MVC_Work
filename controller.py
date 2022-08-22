from model import Model
from view import View


class Controller:
    def __init__(self):

        self.model = Model()
        self.view = View(self)

    def main(self):
        print("Controller - Main")
        self.view.main()

    def on_button_click(self, caption):  # A função de callback, que gerencia o clique de todos os botões
        print(f'Botão {caption} acionado. Função on_button_click')
        result = self.model.execute(caption)  # Está chamando o execute do Model

        self.view.value_var.set(result)  # Estou usando a variável de instância criada em View para poder passar os dados.

    def gerar_pasta(self):
        print("Controller - Gerar Pasta")

    def gerar_gabarito(self):
        print("Controller - Gerar Gabarito")

    def realizar_correcao(self):
        print("Controller - Realizar Correção")

    def exportar_dados(self):
        print("Controller - Exportar Dados")


if __name__ == '__main__':
    controller = Controller()
    controller.main()
