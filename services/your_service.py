"""Module that contains a layer to encasplulate 
tasks that contains businness logic.
COuld call the model if tasks depends on it
"""

import db
import os



class DomaineService:
    def __init__(self, model):

        self.model = model()  # if any could be empty

    def consulta_area(self):

        print("Consulta Área")
        cursor_banco_concurso_area = db.sql_conecta.cursor(buffered=True)
        sql_area = """SELECT area 
        FROM  c
        oncursos.v_concurso_status 
        where  v_concurso_status.status = "EM_ANDAMENTO" 
        and v_concurso_status.tipo = "EXTERNO" and v_concurso_status.inativo = 0 
        and v_concurso_status.data_inicio <= now() 
        and (v_concurso_status.data_validade is null or v_concurso_status.data_validade > now()) order by v_concurso_status.data_inicio desc"""

        cursor_banco_concurso_area.execute(sql_area)
        result_area = cursor_banco_concurso_area.fetchall()
        string = " ".join([str(options) for options in result_area])

        # Precisei de QUATRO FASES de tratamento da string que veio do banco!

        cursor_banco_concurso_area.execute(sql_area)

        trata_string_1 = string.replace("',)", '"')
        trata_string_2 = trata_string_1.replace("('", '"')
        trata_string_3 = trata_string_2.replace("',)", "")
        self.lista_concursos = trata_string_3.replace("('", "")

        cursor_banco_concurso_area.close()

        return self.lista_concursos

    def seleciona_id(self, options):

        cursor = db.sql_conecta.cursor(buffered=True)
        query = 'SELECT id FROM concursos.v_concurso_status where v_concurso_status.area = %s AND v_concurso_status.status = "EM_ANDAMENTO" and v_concurso_status.tipo = "EXTERNO" and v_concurso_status.inativo = 0'
        cursor.execute(query, (options))
        result_id = cursor.fetchone()
        rows = cursor.statement
        # print("Seleciona ID")
        print("Query Executada = ", rows)
        print("Resultado Query = ", result_id)
        cursor.close()
        return result_id

    def gera_pasta(self,path):
        
        if not os.path.exists(path):
            os.makedirs(path)
            return (True, "Diretório criado!")
        else:
            return (False, "Diretório já existe")

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
