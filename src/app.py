from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
app =Flask(__name__)

#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql=MySQL(app)

#Setting
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM contacts")
    if resultValue > 0:
        contacts = cur.fetchall()
        #print(contacts)
        return render_template('index.html', contacts = contacts)
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        # print(fullname, phone, email)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)", (fullname, phone, email))
        mysql.connection.commit()
        cur.close()
        flash('Contacto agregado Satisfactoriamente!')
    return redirect(url_for('index'))
    

@app.route('/edit_contact/<string:id>')
def edit_contact(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM contacts WHERE id = %s", [id])
    contact = cur.fetchone()
    return render_template('edit_contact.html', contact = contact)
    #return f"Edit Contact {id}"

@app.route('/update_contact/<string:id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s", (fullname, phone, email, id))
        mysql.connection.commit()
        cur.close()
        flash('Contacto actualizado Satisfactoriamente!')
    return redirect(url_for('index'))

@app.route('/delete_contact/<id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE id = {id}" .format(id=id))
    mysql.connection.commit()
    cur.close()
    flash(f'Contacto {id} eliminado Satisfactoriamente!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port =3000,debug=True)