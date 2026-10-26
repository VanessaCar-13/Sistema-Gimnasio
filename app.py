from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('gimnasio.db')
    cursor = conn.cursor()
    # Tabla de Usuarios (Basada en tu PDF: PN-04)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            edad INTEGER NOT NULL,
            datos_contacto TEXT NOT NULL,
            estado TEXT DEFAULT 'Habilitado'
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('gimnasio.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    edad = request.form['edad']
    contacto = request.form['contacto']
    
    conn = sqlite3.connect('gimnasio.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (nombre, telefono, edad, datos_contacto) VALUES (?, ?, ?, ?)",
                   (nombre, telefono, edad, contacto))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)