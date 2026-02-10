# Agenda em Python usando Flask 

Este projeto consiste em uma agenda simples desenvolvida em Python utilizando o framework Flask. O objetivo é aplicar e consolidar conhecimentos básicos de desenvolvimento web e programação em Python. Durante o desenvolvimento do projeto, foram trabalhados conceitos como a arquitetura MVC (Model, View, Controller), o uso do framework Flask e seus principais componentes, programação orientada a objetos, variáveis de ambiente e fundamentos da linguagem Python.


Para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork deste repositório, clicando no botão `Fork`.

2. Clone seu repositório localmente:

~~~bash
git clone<url_seu_repositorio>
~~~

3. Abra o projeto utilizando o seu IDE preferido.

4. Crie um ambiente virtual utilizando a versão > 3.12.10 do Python (opcional):

~~~bash
python -m venv .venv 
~~~

5. Ative seu ambiente virtual:

Bash:
~~~bash
source .venv/Scripts/Activate
~~~

PowerShell:
~~~powershell
.\.venv\Scripts\Active.ps1
~~~

6. Instale todas as dependências constantes no arquivo `requirements.txt`:

~~~python
pip install -r requirements.txt
~~~

7. Copie o arquivo `.env.example`, cole na raíz do projeto e renomeie a cópia para `.venv`.

8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Ex.:

~~~env
DATABASE='./data/meubanco.db'
~~~

9. Rode a aplicação no Python, utilizando o comando:

~~~bash
flask run 
~~~

10. Acesse a aplicação no endereço e porta indicados no terminal. Ex.:

`http://127.0.0.1:5000`