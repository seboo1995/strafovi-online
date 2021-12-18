from flask import Flask,render_template,url_for,request
from utils import make_database
import pandas
from flask_sqlalchemy import SQLAlchemy


# make update to the database
make_database('database/baza.csv')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strafovi.db'
db = SQLAlchemy(app)





@app.route('/')
def index():
    with open('categories.txt') as cat:
        categories = cat.readlines()

    categories = [i.strip() for i in categories]
    return render_template('index.html',categories = categories)

@app.route('/<category>')
def category(category):
    if category == 'Штрафови':
        tip_strafovi = db.engine.execute('SELECT * FROM strafovi').all()
        t = set()
        pics = {}
        for tip in tip_strafovi:
            t.add(tip.Ime)
            pics[tip.Ime] = tip.Slika
        print(pics)
        return render_template('categories.html', category='Штрафови', items=t, pictures=pics)

    else:
        return  ("NSASASSASSSS")

@app.route('/product')
def product():
   kategorija  = request.args.get('kategorija', None)
   pod_kategorija = request.args.get('pod_kategorija',None)

   podatoci = db.engine.execute(f'''
   SELECT * FROM {kategorija} WHERE Ime = {pod_kategorija}
   ''')

   return render_template('')


if __name__ == '__main__':
    app.run(debug=True)