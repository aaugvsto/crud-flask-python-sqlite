import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("agenda.db")
    except sqlite3.error as e:
        print(e)
    return conn

# http://127.0.0.1:5000/
@app.route('/')
def bemVindo():
    return "<h1>Bem vindo a sua agenda de contatos</h1><br><a href='http://127.0.0.1:5000/contatos'>Ir para minha agenda de contatos</a>"

# http://127.0.0.1:5000/contatos
@app.route('/contatos', methods=['GET'])
def mostraContatos():
    conn = db_connection()
    query = "SELECT id, nome, telefone, email, empresa FROM contatos"
    cursor = conn.execute(query)
    contatos = [
        dict(id=row[0], nome=row[1], telefone=row[2], email=row[3], empresa=row[4])
        for row in cursor.fetchall()
    ]
    if contatos is not None:
        return jsonify(contatos)

# http://127.0.0.1:5000/contatos/buscar?nome=teste
@app.route('/contatos/buscar', methods=['GET'])
def buscaContato():
    nomeCtt = request.args.get('nome')
    conn = db_connection()
    query = "SELECT * FROM contatos WHERE nome LIKE '%{}%'".format(nomeCtt)
    cursor = conn.execute(query)
    contatos = [
        dict(id=row[0], nome=row[1], empresa=row[2], telefone=row[3], email=row[4])
        for row in cursor.fetchall()
    ]
    if contatos is not None:
        return jsonify(contatos)

# http://127.0.0.1:5000/contatos/criar?nome=teste&empresa=teste&telefone=123&email=teste
@app.route('/contatos/criar', methods=['POST'])
def criaContato():
    nome = request.args.get('nome')
    empresa = request.args.get('empresa')
    telefone = request.args.get('telefone')
    email = request.args.get('email')

    conn = db_connection()
    query = "INSERT INTO contatos (id, nome, empresa, telefone, email) VALUES (NULL ,'{0}', '{1}', '{2}', '{3}')".format(nome, empresa, telefone, email)
    conn.execute(query)
    conn.commit()
    conn.close()
    return "<h1>Sucesso! Contato {} inserido na sua agenda</h1>".format(nome)


# http://127.0.0.1:5000/contatos/atualizar?id=4?nome=teste&empresa=teste&telefone=123&email=teste
@app.route('/contatos/atualizar', methods=['PUT'])
def atualizaContato():
    id = request.args.get('id')
    nome = request.args.get('nome')
    telefone = request.args.get('telefone')
    email = request.args.get('email')
    empresa = request.args.get('empresa')
    conn = db_connection()

    query = """UPDATE contatos SET nome = '{0}' and empresa='{1}' and telefone='{2}' and email='{3}' WHERE id = {4}""".format(nome, empresa, telefone, email, id)
    conn.execute(query)
    conn.commit()
    conn.close()
    return "<h1>Contato {} atualizado com sucesso!</h1>".format(id)

@app.route("/contatos/excluir", methods=["DELETE"])
def deletaContato():
    idCtt = request.args.get('id')
    conn = db_connection()
    query = """DELETE FROM contatos WHERE id = {}""".format(idCtt)
    conn.execute(query)
    conn.commit()
    conn.close()
    return "<h1> Contato {} excluido com sucesso da sua agenda </h1>".format(idCtt)


if __name__ == "__main__":
    app.run()