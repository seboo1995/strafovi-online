from flask import Flask,render_template,url_for,request
from utils import make_database
import pandas
from flask_sqlalchemy import SQLAlchemy


# make update to the database
make_database('database/baza.csv',name='strafovi')
make_database('database/sajmni.csv', name='sajmni')
make_database('database/navrtki.csv', name='navrtki')
make_database('database/pop_ntini.csv', name='pop_nitni')


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

    elif category == 'Подлошки(Шајмни)':
        tip_sajmni = db.engine.execute('SELECT * FROM sajmni').all()
        t = set()
        pics = {}
        for tip in tip_sajmni:
            t.add(tip.Ime)
            pics[tip.Ime] = tip.Slika
        print(pics)
        return render_template('categories.html', category='Подлошки(шајмни)', items=t, pictures=pics)

    elif category == 'Навртки':
        tip_navrtki = db.engine.execute('SELECT * FROM navrtki').all()
        t = set()
        pics = {}
        for tip in tip_navrtki:
            t.add(tip.Ime)
            pics[tip.Ime] = tip.Slika
        print(pics)
        return render_template('categories.html', category='Навртки', items=t, pictures=pics)

    elif category == 'Поп нитни':
        tip_nitni = db.engine.execute('SELECT * FROM pop_nitni').all()
        t = set()
        pics = {}
        for tip in tip_nitni:
            t.add(tip.Ime)
            pics[tip.Ime] = tip.Slika
        print(pics)
        return render_template('categories.html', category='Поп нитни', items=t, pictures=pics)

    else:
        return 'Under Construction'




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