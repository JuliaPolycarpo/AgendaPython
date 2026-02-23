from sqlite3 import Cursor
from models.database import Database
from typing import Optional, Self
from datetime import datetime


class Tarefa:

    def __init__(self: Self,
                 titulo_tarefa: Optional[str],
                 data_conclusao: Optional[str] = None,
                 estado_tarefa: Optional[bool] = False,
                 concluida_em: Optional[str] = None,
                 id_tarefa: Optional[int] = None) -> None:
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao
        self.id_tarefa = id_tarefa
        self.estado_tarefa = bool(estado_tarefa)
        self.concluida_em = concluida_em

    def salvar_tarefa(self) -> None:
        with Database() as db:
            query = '''
                INSERT INTO tarefas
                (titulo_tarefa, data_conclusao, estado_tarefa, concluida_em)
                VALUES (?, ?, ?, ?);
            '''
            db.executar(query, (self.titulo_tarefa, self.data_conclusao, self.estado_tarefa, self.concluida_em))

    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query = '''
                UPDATE tarefas
                SET titulo_tarefa = ?, data_conclusao = ?
                WHERE id = ?;
            '''
            return db.executar(query, (self.titulo_tarefa, self.data_conclusao, self.id_tarefa))

    def excluir_tarefa(self) -> Optional[Cursor]:
        if self.estado_tarefa:
            return None  # bloqueia exclusão
        with Database() as db:
            query = 'DELETE FROM tarefas WHERE id = ?;'
            return db.executar(query, (self.id_tarefa,))

    def alterar_estado(self) -> None:
        with Database() as db:
            if self.estado_tarefa:
                # Reabrir tarefa
                query = '''
                    UPDATE tarefas
                    SET estado_tarefa = 0, concluida_em = NULL
                    WHERE id = ?;
                '''
                db.executar(query, (self.id_tarefa,))
                self.estado_tarefa = False
                self.concluida_em = None
            else:
                # Concluir tarefa
                agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query = '''
                    UPDATE tarefas
                    SET estado_tarefa = 1, concluida_em = ?
                    WHERE id = ?;
                '''
                db.executar(query, (agora, self.id_tarefa))
                self.estado_tarefa = True
                self.concluida_em = agora

    @classmethod
    def buscar_por_id(cls, id_tarefa: int) -> Optional[Self]:
        with Database() as db:
            query = 'SELECT * FROM tarefas WHERE id = ?;'
            resultado = db.buscar_tudo(query, (id_tarefa,))
            if not resultado:
                return None

            # Banco: id, titulo_tarefa, data_conclusao, estado_tarefa, concluida_em
            id_, titulo, data, estado, concluida = resultado[0]

            return cls(
                titulo_tarefa=titulo,
                data_conclusao=data,
                estado_tarefa=estado,
                concluida_em=concluida,
                id_tarefa=id_
            )

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query = 'SELECT * FROM tarefas;'
            resultados = db.buscar_tudo(query)

            tarefas = []
            for row in resultados:
                id_, titulo, data, estado, concluida = row
                tarefas.append(
                    cls(
                        titulo_tarefa=titulo,
                        data_conclusao=data,
                        estado_tarefa=estado,
                        concluida_em=concluida,
                        id_tarefa=id_
                    )
                )
            return tarefas
         