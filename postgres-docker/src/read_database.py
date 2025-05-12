import psycopg2
import time
import pandas as pd
import os

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
            print("Conectado ao PostgreSQL")
            return conn
        except psycopg2.OperationalError as e:
            tentativas -= 1
            print(f"Erro ao conectar ao banco: {e}")
            time.sleep(2)

    raise Exception("Erro ao conectar ao banco")

def fetch_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    cursor.close()

    return pd.DataFrame(data, columns=columns)

def read_csv_file(csv_path):
    if os.path.exists(csv_path):
        print(f"Lendo arquivo CSV: {csv_path}")
        df = pd.read_csv(csv_path)
        print(df)
    else:
        print(f"Arquivo CSV não encontrado em {csv_path}")

def main():
    conn = connect_to_db()
    tables = ['usuarios']

    for table in tables:
        print(f"\n--- Tabela {table} ---")
        df = fetch_data(conn, table)
        print(df)

    csv_path = '/usr/src/app/dados/data.csv'  
    read_csv_file(csv_path)

    print("Execução concluída. Container continuará rodando...")
    time.sleep(999999) 

if __name__ == "__main__":
    main()
