from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/OKAN/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))



@app.route("/index")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

class Okan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(80))
    soyisim = db.Column(db.String(100))
    memleket = db.Column(db.String(120))

@app.route("/add",methods=["POST"])
def addtodo():
    title = request.form.get("title")
    newtodo = Todo(title = title,complete = False)
    db.session.add(newtodo)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

  
