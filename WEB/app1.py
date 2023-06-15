from flask import Flask, render_template, request
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'foo'
app.config['MYSQL_DB'] = 'SAE41'

  

mysql = MySQL(app)

@app.route("/")
def render():
	return render_template('forms.html')


@app.route("/liste_r")
def rennder():
	return rennder_template('liste_r.html')





@app.route("/ajouter_r")
def rennnder():
	return rennnder_template('ajouter_r.html')


