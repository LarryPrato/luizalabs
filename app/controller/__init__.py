import os
from flask import  render_template,send_file, request, Blueprint,  abort, send_from_directory
from jinja2 import TemplateNotFound
import matplotlib.pyplot as plt
from io import BytesIO
import app.logic as logic
from app import app, conexoes
from app import database

appBp = Blueprint('appBp', __name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/vertices', methods=['GET'])
def vertices():
    try:
        resultado = logic.mostrar_total_vertices(conexoes)
        return render_template('page1.html', resultado_text=f'Os nomes das pessoas do grafo são:  {resultado}')
    except TemplateNotFound:
        abort(404)

@app.route('/grafo', methods=['GET'])
def grafo():
    try:
        fig = logic.mostrar_grafo(conexoes)
        img = BytesIO()
        plt.savefig(img)
        img.seek(0)
        plt.clf()
        return send_file(img, mimetype='image/png')
    except TemplateNotFound:
        abort(404)

@app.route('/vizinhos/submit', methods=['GET', 'POST'])
def vizinhos():
    try:
        nome = request.form['nodo_1']
        resultado = logic.mostrar_amigos(conexoes, nome)
        return render_template('page2.html', vizinhos_text=f'Os vizinhos de {nome} são:  {resultado}')
    except TemplateNotFound:
        abort(404)    

@app.route('/vizinhos', methods=['GET'])
def vizinhosPage():
    try:
        return render_template('page2.html')
    except TemplateNotFound:
        abort(404)

@app.route('/relacionados/submit', methods=['GET', 'POST'])
def relacionados():
    try:
        nome = request.form['nodo_2']
        resultado = logic.mostrar_amigos_de_amigos(conexoes, nome)
        return render_template('page3.html', relacionados_text=f'Os vizinhos dos vizinhos de {nome} são:  {resultado}' )
    except TemplateNotFound:
        abort(404)

@app.route('/relacionados', methods=['GET'])
def relacionadosPage():
    try:
        return render_template('page3.html')
    except TemplateNotFound:
        abort(404)

@app.route('/cadastro/submit', methods=['POST'])
def cadastro():
    try:
        usuario1 = request.form['novo_usuario']
        usuarios = request.form['contatos'] 
        output= conexoes.cadastrar_usuario_e_conexoes(usuario1, usuarios.split(", "))
        conn = database.get_db_connection()
        for item in usuarios.split(", "):
            if item in conexoes.frame().values:
                conn.execute('INSERT INTO conexoes (usuario_1, usuario_2) VALUES (?, ?)', (usuario1, item))
        conn.commit()
        conn.close()
        return render_template('page4.html', resultado_cadastro = output)
    except TemplateNotFound:
        abort(404)

@app.route('/cadastro', methods=['GET'])
def cadastroPage():
    try:
        return render_template('page4.html')
    except TemplateNotFound:
        abort(404)

@app.route('/table', methods=['GET'])
def show_table():
    try:
        df = conexoes.frame()
        return render_template('table.html',  datatable=df.to_dict(orient='records'))
    except TemplateNotFound:
        abort(404)

@app.route('/database' , methods=['GET'])
def show_database():    
    try:
        conn = database.get_db_connection()
        registros = conn.execute('SELECT * FROM conexoes').fetchall()
        conn.close()
        return render_template('database.html', registros=registros)

    except TemplateNotFound:
        abort(404)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')