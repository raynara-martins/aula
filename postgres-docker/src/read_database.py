import psycopg2
import time
import pandas as pd

time.sleep(5)

def connect_to_db():
    tentativas = 2
    while tentativas > 0:
        try:
            conn = psycopg2.connect(
                host="db",
                database="meubanco",
                user="postgres",
                password="senha_segura"
            )
            print("Conectado")
            return conn
        except psycopg2.OperationalError as e:
            tentativas -= 1
            print(f"Erro: {e}")
            time.sleep(2)

    raise Exception("Erro ao conectar ao banco")

def fetch_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    cursor.close()

    return pd.DataFrame(data, columns=columns)

def main():
    conn = connect_to_db()
    tables = ['usuarios']

    for table in tables:
        print(f"\n--- Tabela {table} ---")
        df = fetch_data(conn, table)
        print(df)

while True:
    main()
