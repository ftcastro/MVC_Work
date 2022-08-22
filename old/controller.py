import db
import os
import tkinter as tk

from tkinter import messagebox
from models import Model
from views import View


class Controller:

    def __init__(self):

        print("Init - Controller")
        self.model = Model()
        self.view = View()

        # Pass to view.py links on root frame and controller object

    def consulta_area(self):

        print("Consulta Área")
        cursor_banco_concurso_area = db.sql_conecta.cursor(buffered=True)
        sql_area = 'SELECT area FROM  concursos.v_concurso_status where  v_concurso_status.status = "EM_ANDAMENTO" and v_concurso_status.tipo = "EXTERNO" and v_concurso_status.inativo = 0 and v_concurso_status.data_inicio <= now() and (v_concurso_status.data_validade is null or v_concurso_status.data_validade > now()) order by v_concurso_status.data_inicio desc'
        cursor_banco_concurso_area.execute(sql_area)
        result_area = cursor_banco_concurso_area.fetchall()
        string = " ".join([str(options) for options in result_area])

        # Precisei de QUATRO FASES de tratamento da string que veio do banco!

        cursor_banco_concurso_area.execute(sql_area)

        trata_string_1 = string.replace("',)", "\"")
        trata_string_2 = trata_string_1.replace("('", "\"")
        trata_string_3 = trata_string_2.replace("',)", "")
        self.lista_concursos = trata_string_3.replace("('", "")

        cursor_banco_concurso_area.close()

        print("Drop Current = ", View.tela1.drop.current())

        return self.lista_concursos

    def seleciona_id(self, lista_concursos):

        self.options = View.telas.option

        # options = self.lista_concursos
        print("Option = ", self.option)
        # options = "TOPÓGRAFO"
        cursor = db.sql_conecta.cursor(buffered=True)
        query = 'SELECT id FROM concursos.v_concurso_status where v_concurso_status.area = %s AND v_concurso_status.status = "EM_ANDAMENTO" and v_concurso_status.tipo = "EXTERNO" and v_concurso_status.inativo = 0'
        cursor.execute(query, (self.options,))
        self.result_id = cursor.fetchone()
        rows = cursor.statement

        # print("Seleciona ID")
        print("Query Executada = ", rows)
        print("Resultado Query = ", self.result_id)
        cursor.close()

        return self.option

    def gera_pasta(self):

        id_pasta = Controller.seleciona_ID.result_id[0]

        print("ID Pasta = ", id_pasta)

        path = 'H:/DIN/Fernando/concursos/teste'

        isExist = os.path.exists(path)

        if not isExist:
            os.makedirs(path)
            tk.messagebox.showinfo(title='Correção de Provas - URBAM', message='Diretório criado com sucesso.')
            print("Diretório criado!")
        else:
            tk.messagebox.showwarning(title='Correção de Provas - URBAM', message='O diretório já existe.')
            print("Diretório já existe")
        pass

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

