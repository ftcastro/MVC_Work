class Model:

    def __init__(self):

        self.path = 'C:/users/fernando.castro/desktop/concursos/teste'
        self.value = ''
        self.pasta_gerada = None

    def execute(self, caption):  # Método público execute. Vai ser acessado de fora da classe.
        print(f'Executando comando: {caption} função execute')

        if caption == 'Gerar Pasta':
            print(f'{caption} acionado. if caption...')
            self.pasta_gerada = True
            # self.gerar_pasta()

            return self.pasta_gerada

        elif caption == 'Gerar Gabarito':
            print(f'{caption} acionado. if caption...')
            # self.gerar_gabarito()

        elif caption == 'Realizar Correção':
            print(f'{caption} acionado. if caption...')
            # self.realizar_correcao()

        elif caption == 'Exportar Dados':
            print(f'{caption} acionado. if caption...')
            # self.exportar_dados()

        else:
            if self.value:  # Aqui eu estou verificando se o valor atual não está vazio. Ao se utilizar apenas if self.value, é o mesmo que comparar se self.value é True
                self.operator = caption

                self.previous_value = self.value

                self.value = ''  # Aqui, após o operador ser pressionado, o display é limpo para que o próximo operador seja exibido e o resultado seja visível

        return self.value
