from models.database import Database
from typing import Self

class Tarefa:
    def __init__(self:Self , titulo_tarefa: str, data_conclusao: str = None) -> None:
        self.titulo_tarefa: str = titulo_tarefa
        self.data_conclusao: str = data_conclusao

    def salvar_tarefa (self: Self) -> None:
        with Database ('./data/tarefas.sqlite3') as db:
            query: str = 'INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);'
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)
