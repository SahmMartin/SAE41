from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'foo'
app.config['MYSQL_DB'] = 'SAE41'
mysql = MySQL(app)



@app.route("/", methods = ["POST", "GET"])
def connection():
	if request.method== "POST":
		username = request.form["username"]
		password = request.form["password"]
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


@app.route("/liste_r.html", methods = ["POST", "GET"])
def liste():
	return render_template('liste_r.html')






