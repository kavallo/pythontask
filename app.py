from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/task.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20))
    clave = db.Column(db.String(20))

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/acceder-login', methods=['POST'])
def accederlogin():
    login = Login.query.filter_by(user=request.form['pass'], clave=request.form['pass'])
    

    
    if 1==2: 
        return redirect(url_for('home'))
    
    return redirect(url_for('login'))
    

@app.route('/create-task', methods=['POST'])
def create():
    task = Task(content=request.form['content'], done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done/<id>')
def done(id):
    task = Task.query.filter_by(id=(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    task=Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)