from flask import Flask, render_template, request
from models.tarefa import Tarefa

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    tarefa = None
    if request.method == 'POST':
        titulo_tarefa = request.form['titulo_tarefa']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()
    
    return render_template('agenda.html', titulo='Agenda', tarefa=tarefa)

@app.route('/Hello')
def hello_world():
    return 'Hello, World!'