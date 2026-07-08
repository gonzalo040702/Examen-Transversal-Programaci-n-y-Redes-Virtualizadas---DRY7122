from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def agregar_usuario(nombre, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    hash_password = generate_password_hash(password)
    c.execute('INSERT INTO usuarios (nombre, password) VALUES (?, ?)',
              (nombre, hash_password))
    conn.commit()
    conn.close()
    print(f"Usuario '{nombre}' agregado con hash: {hash_password}")

def validar_usuario(nombre, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT password FROM usuarios WHERE nombre = ?', (nombre,))
    resultado = c.fetchone()
    conn.close()
    if resultado and check_password_hash(resultado[0], password):
        return True
    return False

@app.route('/')
def index():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT id, nombre, password FROM usuarios')
    usuarios = c.fetchall()
    conn.close()
    html = '<h1>Usuarios Registrados</h1><table border=1>'
    html += '<tr><th>ID</th><th>Nombre</th><th>Hash Password</th></tr>'
    for u in usuarios:
        html += f'<tr><td>{u[0]}</td><td>{u[1]}</td><td>{u[2]}</td></tr>'
    html += '</table>'
    return html

if __name__ == '__main__':
    init_db()
    # Agregar integrantes del grupo
    agregar_usuario('Gonzalo', 'pass123')
    agregar_usuario('Daniel', 'pass456')

    # Validar usuarios
    print("\n===== VALIDACIÓN DE USUARIOS =====")
    print(f"Gonzalo válido: {validar_usuario('Gonzalo', 'pass123')}")
    print(f"Daniel válido: {validar_usuario('Daniel', 'pass456')}")
    print(f"Intento inválido: {validar_usuario('Gonzalo', 'incorrecta')}")

    print("\n Servidor iniciado en http://localhost:7500")
    app.run(port=7500, debug=True)
