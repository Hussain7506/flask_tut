from flask import Flask, render_template,request,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'valarmorghulis'

db = SQLAlchemy(app)

# Define your models here
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    decs = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/")
def hello_world():
    return render_template("test.html")

@app.route("/html",methods=["GET","POST"])
def show_html():    
    if request.method=="POST":
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo(title=title,decs=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo=Todo.query.all()
    flash("Delete Successful","success")
    return render_template("index.html",alltodo=alltodo)


@app.route("/delete/<int:sno>",methods=["GET"])
def delete(sno):
    flash("Delete Successful","success")
    return redirect("/html")

if __name__ == "__main__":
    app.run(debug=True)
