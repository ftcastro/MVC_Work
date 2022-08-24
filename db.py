import mysql.connector
import mysql.connector.pooling
from mysql.connector import Error

# Dados da conexão e do pool

poolname = "mysqlpool"
poolsize = 10
host = 'localhost'
port = 5432
user = "---"
password = "---"
database = "---"

# Pool de Conexões

# String de Conexão

try:
    sql_conecta = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        raise_on_warnings=True,
    )
    cursor = sql_conecta.cursor()
except:
    pass
