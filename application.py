from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key="flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'crud'
app.config['MYSQL_PASSWORD'] = 'Macron2020!'
app.config['MYSQL_DB'] = 'cruddb'

mysql=MySQL(app)


@app.route('/')
def index():
    cur=mysql.connection.cursor()
    cur.execute("select * from students")
    data=cur.fetchall()
    cur.close()
    return render_template('index.html', students = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data inserted successfully")
        name =  request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("insert into students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
