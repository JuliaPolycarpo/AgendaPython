from sqlite3 import Cursor
from tkinter import N
from models.database import Database
from typing import Self, Any, Optional


class Tarefa:
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None, id_tarefa: Optional[int] = None) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa

    # Tarefa(titulo_tarefa="Nova Tarefa")
    # Tarefa(titulo_tarefa="Outra tarefa", data_conclusao="2026-02-03")
    # Tarefa(id_tarefa=1)

    @classmethod
    def id(cls, id: int) -> Self:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado: list[Any]= db.buscar_tudo(query, params)

            #Desempacotamento de coleção
            [[titulo, data]] = resultado

        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data)
    
    # Simulando conceito de sobrecarga
    # Tarefa('Titulo Tarefa')
    # Tarefa('Titulo Tarefa', '2026-02-03')
    # Tarefa.id(1)



    def salvar_tarefa(self: Self) -> None:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data) for titulo, data in resultados]
            return tarefas 
        
    def excluir_tarefa(self) -> Cursor:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado