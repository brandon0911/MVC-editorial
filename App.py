from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        numero_celular = request.form['numero_celular']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (nombre, numero_celular, email) VALUES (%s,%s,%s)", (nombre, numero_celular, correo))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['nombre']
        phone = request.form['numero_celular']
        email = request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute("""
            Actualizar contactos
            Nombre = %s,
                correo = %s,
                numero_celular = %s
            identificacion = %s
        """, (fullname, email, phone, id))
        flash('Contacto actualizado con éxito')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('eliminar contacto id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado con éxito')
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
