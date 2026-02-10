from sqlite3 import Cursor
from tkinter import N
from models.database import Database
from typing import Self, Any, Optional


class Tarefa:
    """Classe que representa uma tarefa, com métodos para salvar, obter, excluir e atualizar tarefas de dados no banco de dados usando a classe `Database`."""
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None, id_tarefa: Optional[int] = None) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa

    # Tarefa(titulo_tarefa="Nova Tarefa")
    # Tarefa(titulo_tarefa="Outra tarefa", data_conclusao="2026-02-03")
    # Tarefa(id_tarefa=1)

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
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
        with Database() as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, id FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data, id) for titulo, data, id in resultados]
            return tarefas 
        
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        

    def atualizar_tarefa(self) -> Cursor:
        with Database () as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ? WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado 
            
