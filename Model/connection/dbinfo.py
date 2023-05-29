import psycopg2

# Definir as informações de conexão
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="alicenha",
    host="localhost",
    port="5432"
)