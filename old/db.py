import mysql.connector
import mysql.connector.pooling
from mysql.connector import Error

# Dados da conexão e do pool

poolname = 'mysqlpool'
poolsize = 10
host = '191.252.58.98'
port = '3306'
user = 'root'
password = 'SmgoQu33n!'
database = 'concursos'

# Pool de Conexões

try:
    connectionpool = mysql.connector.pooling.MySQLConnectionPool(pool_name=poolname,
                                                                 pool_size=poolsize,
                                                                 pool_reset_session=True,
                                                                 host=host, port=port,
                                                                 user=user,
                                                                 password=password,
                                                                 database=database)

    connectionpool = connectionpool.get_connection()
    cursorpool = connectionpool.cursor()

except Error as e:
    print("Erro no pool de conexões: ", e)

finally:
    if connectionpool.is_connected():
        cursorpool.close()
        connectionpool.close()

# String de Conexão

sql_conecta = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database, raise_on_warnings=True)
cursor = sql_conecta.cursor()