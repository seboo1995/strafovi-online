from flask import Flask,render_template,url_for,request
from utils import make_database
import pandas
from flask_sqlalchemy import SQLAlchemy


# make update to the database
make_database('database/baza.csv')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strafovi.db'
db = SQLAlchemy(app)



with open('categories.txt') as cat:
    categories = cat.readlines()


@app.route('/')
def index():
    return render_template('index.html',categories = categories)

@app.route('/<category>')
def category(category):
    if category == 'strafovi':
        k = db.engine.execute('SELECT * FROM strafovi WHERE Ime LIKE "%штраф%"').all()

    else:
        return  ("NSASASSASSSS")




if __name__ == '__main__':
    app.run(debug=True)