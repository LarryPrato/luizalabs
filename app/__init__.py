from flask import Flask, render_template
from app import logic
from app import database

### Bloco executado no inicio da app para mostrar os nomes com  grafo requerido.
conexoes = logic.Conexoes()
conexoes.criar_conexao('Ana', 'João')
conexoes.criar_conexao('Ana', 'Carlos')
conexoes.criar_conexao('Ana' , 'Maria')
conexoes.criar_conexao('Ana' , 'Vinicius')
conexoes.criar_conexao('Ana' , 'Maria')
conexoes.criar_conexao('Vinicius', 'Maria')
conexoes.criar_conexao('João' , 'Luiza')

conn = database.get_db_connection()
for index, row in conexoes.frame().iterrows():
    usuario_1, usuario_2 = (row['usuario_1'], row['usuario_2'])
    conn.execute('INSERT INTO conexoes (usuario_1, usuario_2) VALUES (?, ?)',
             (usuario_1, usuario_2))
conn.commit()
conn.close()
#########

app = Flask(__name__)

from app.controller import appBp
app.register_blueprint(appBp)
# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404