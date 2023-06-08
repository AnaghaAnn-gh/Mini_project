from flask import Flask,request,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html')
database={'helloworld@gmail.com':'123','hello@gmail.com':'345','mean@gmail.com':'average'}

@app.route('/index1',methods=['POST','GET'])
def login():
	name1=request.form['username']
	pwd=request.form['password']
	if name1 not in database:
		return render_template('home.html',info='Invalid User')
	else:
		if database[name1]!=pwd:
			return render_template('home.html',info='Invalid Password')
		else:
			return render_template('index1.html',username=name1)

if __name__ == '__main__':
    app.run(debug=True)