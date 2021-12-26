from flask import Flask,render_template,url_for,request
from utils import make_database
import pandas
from flask_sqlalchemy import SQLAlchemy


map_name = {
    'Штрафови':'strafovi',
    'Навртки':'navrtki',
    'Подлошки(Шајмни)':'sajmni',
    'Поп нитни':'pop_nitni',
    'Осигурачи':'osiguraci'
}
map_col_names = {
    'Ime': 'Име',
    'Za': 'За',
    'Debelina': 'Дебелина',
    'Dolzina': 'Должина',
    'Glava': 'Глава',
    'Cena': 'Цена',
    'Dimenzija':'Димензија',
    'Sirocina': 'Широчина',
    'ID':'ID',
    'Navoj(cekor)':'Навој(Чекор)',
    'Golemina':'Големина'

}

# make update to the database
make_database('database/baza.csv',name='strafovi')
make_database('database/sajmni.csv', name='sajmni')
make_database('database/navrtki.csv', name='navrtki')
make_database('database/pop_ntini.csv', name='pop_nitni')
make_database('database/osiguraci.csv', name='osiguraci')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strafovi.db'
db = SQLAlchemy(app)





@app.route('/')
def index():
    with open('categories.txt') as cat:
        categories = cat.readlines()

    categories = [i.strip() for i in categories]
    return render_template('index.html',categories = categories)

@app.route('/kategorija/<category>')
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
        return render_template('categories.html', category='Подлошки(Шајмни)', items=t, pictures=pics)

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

    elif category == 'Осигурачи':
        tip_osiguraci = db.engine.execute('SELECT * FROM osiguraci').all()
        t = set()
        pics = {}
        for tip in tip_osiguraci:
            t.add(tip.Ime)
            pics[tip.Ime] = tip.Slika
        print(pics)
        return render_template('categories.html', category='Осигурачи', items=t, pictures=pics)

    else:
        return 'Under Construction'




@app.route('/product/<kategorija>/<pod_kategorija>')
def product(kategorija,pod_kategorija):
    query = db.engine.execute(f'SELECT* FROM "{map_name[kategorija]}" WHERE Ime="{pod_kategorija}"').all()
    slika = query[0].Slika

    keys = [i for i in query[0].keys() if i!='Slika' and i!='index']
    products = []
    for prod in query:
        temp = {x:prod[x] for x in keys}
        products.append(temp)
    keys = [map_col_names[i.strip()] for i in keys]
    return render_template('product.html',kategorija=kategorija, pod_kategorija=pod_kategorija,products = products, slika=slika, columns=keys)


if __name__ == '__main__':
    app.run(debug=True)