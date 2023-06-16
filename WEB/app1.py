from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'foo'
app.config['MYSQL_DB'] = 'SAE41'
mysql = MySQL(app)



@app.route("/", methods = ["POST", "GET"])
def forms():
	return forms_template('forms.html')

	if request.method== "POST":
		username = request.form["name"]
		password = request.form["pwd"]
		cursor = mysql.connection.cursor()
		query = "SELECT username, password FROM users WHERE username = %s AND pwd = %s"
		cursor.execute(query, (name, pwd))
		result = cursor.fetchall()
		cursor.close()

		if result is not None: 
			return render_template("liste_r.html")
		else:
			return render_template("forms.html")

	return render_template("forms.html")


@app.route("/liste_r")
def liste():
	return render_template('liste_r.html')





@app.route("/ajout_r")
def ajout():
	return render_template('ajout_r.html')


