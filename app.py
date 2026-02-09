from flask import Flask, redirect, render_template, request, url_for
from models.tarefa import Tarefa

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo_tarefa']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    terefa = Tarefa.id(idTarefa)
    terefa.excluir_tarefa()
    #return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)
    return redirect(url_for('agenda'))

@app.route('/Hello')
def hello_world():
    return 'Hello, World!'

  
@app.route('/update/<int:idTarefa>', methods = ['GET', 'POST'])
def update(idTarefa):
    if request.method == 'POST':
        titulo = request.form['titulo_tarefa']
        data = request.form['data_conclusao']
        tarefa = Tarefa(titulo, data, idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for('agenda'))
    
    tarefas=Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)
    return render_template('agenda.html', titulo=f'Editando a tarefa ID: {idTarefa}', tarefas=tarefas, tarefa_selecionada=tarefa_selecionada)

