from sqlite3 import Connection, connect, Cursor
from typing import Any

class Database: 
    def __init__(self, db_name: str) -> None:
        self.connection: Connection = connect (db_name)
        self.cursor = self.connection.cursor()

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    
    def buscar_tudo (self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self) -> None:
        self.connection.close()

# Métodos para o gerenciamento do contexto 
    # Método de entrada no contexto
    def __enter__(self):
        print('Conexão aberta com o banco de dados.')
        return self

    #Método de saída do contexto
    def __exit__(self, exc_type, exc_value, traceback):
        print('Conexão fechada com o banco de dados.')
        self.close()

# # Área de teste
# try: 
#     db = Database('./data/tarefas.sqlite3')
#     db.executar('''
# CREATE TABLE IF NOT EXISTS tarefas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     titulo_tarefa TEXT NOT NULL,
#     data_conclusao TEXT);
# ''')
    
#     db.executar("INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);", ('Estudar Python', '2026-02-02'))
# except Exception as e:
#     print(f'Erro ao criar a tabela: {e}')
#     db.close()
# finally:
#     db.close()