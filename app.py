from flask import Flask, redirect, render_template, request, url_for, flash
from models.database import init_db
from models.tarefa import Tarefa
import os

app = Flask(__name__)

init_db()
app.secret_key = os.environ.get("SECRET_KEY", "uma_chave_padrao_para_dev")


@app.route("/", methods=["GET", "POST"])
def agenda():

    if request.method == "POST":
        titulo_tarefa = request.form["titulo_tarefa"]
        data_conclusao = request.form["data_conclusao"]

        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

        return redirect(url_for("agenda"))

    tarefas = Tarefa.obter_tarefas()
    return render_template("agenda.html", titulo="Agenda", tarefas=tarefas)


@app.route("/delete/<int:idTarefa>")
def delete(idTarefa):

    tarefa = Tarefa.buscar_por_id(idTarefa)

    if not tarefa:
        flash("Tarefa não encontrada.")
        return redirect(url_for("agenda"))

    if tarefa.estado_tarefa:
        flash("Não é possível excluir uma tarefa concluída. Reabra antes.")
        return redirect(url_for("agenda"))

    tarefa.excluir_tarefa()

    flash("Tarefa excluída com sucesso.")
    return redirect(url_for("agenda"))


@app.route("/update/<int:idTarefa>", methods=["GET", "POST"])
def update(idTarefa):

    if request.method == "POST":
        titulo = request.form["titulo_tarefa"]
        data = request.form["data_conclusao"]

        tarefa = Tarefa(titulo, data, id_tarefa=idTarefa)
        tarefa.atualizar_tarefa()

        return redirect(url_for("agenda"))

    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.buscar_por_id(idTarefa)

    return render_template(
        "agenda.html",
        titulo=f"Editando a tarefa ID: {idTarefa}",
        tarefas=tarefas,
        tarefa_selecionada=tarefa_selecionada,
    )


@app.route("/alterar_estado/<int:idTarefa>", methods=["POST"])
def alterar_estado(idTarefa):

    tarefa = Tarefa.buscar_por_id(idTarefa)

    if not tarefa:
        return redirect(url_for("agenda"))

    tarefa.alterar_estado()

    return redirect(url_for("agenda"))
