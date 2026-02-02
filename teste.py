from models.database import Database

#Teste Gerenciador de Contexto 
with Database('./data/tarefas.sqlite3') as db:
    db.executar('INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);', 
                    ('Usar o gerenciador de contexto', '2026-02-03')
                )
    

