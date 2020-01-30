from flask import Flask, render_template, request
from databases import * 

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/laugh_profile')
def laugh_profile():
	return render_template("laugh_profile.html")

@app.route('/add_yourself', methods= ['GET' , 'POST'])
def add_yourself():
	if request.method == 'GET':
		return render_template("add_yourself.html")
	else:
		name= request.form["first-name"]+" "+request.form["last-name"]
		age = int(request.form["age"])
		gender = request.form["gender"]
		hobby = request.form["hobby"]
		add_User(name, gender, age, hobby)
		print(name, age, gender, hobby)
		return render_template('add_yourself.html')

if __name__ == '__main__':
	app.run(debug=True)

