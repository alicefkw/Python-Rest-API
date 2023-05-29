import connection.dbinfo as dbinfo

conn = dbinfo.conn

class Queries():
    def select_table(table):
        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Executar um comando SQL
        cursor.execute(f'SELECT * FROM {table}')

        # Obter os resultados
        rows = cursor.fetchall()

        # Exibir os resultados
        for row in rows:
            print(row)

        # Fechar a conexão
        conn.close()