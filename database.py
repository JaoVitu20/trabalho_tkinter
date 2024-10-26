import sqlite3

def conectar():

    try:
        conn = sqlite3.connect('missoes.db')  # Conecta ou cria o banco de dados
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela():

    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS missoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_lancamento DATE NOT NULL,
                destino TEXT NOT NULL,
                estado TEXT NOT NULL,
                tripulacao TEXT NOT NULL,
                carga_util TEXT NOT NULL,
                duracao TEXT NOT NULL,
                custo REAL NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()  # Confirma as alterações no banco de dados
        conn.close()  # Fecha a conexão
