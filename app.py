from flask import Flask,render_template
from helper import read_data


app = Flask(__name__)

strafovi = read_data('strafovi')
muteri = read_data('muteri')

with open('kategorii.txt') as f:
    kategorii = f.readlines()
d = {}

for i in kategorii:
    kategorija,slika = i.split(',')
    d[kategorija] = slika


@app.route('/')
def index():
    for i in kategorii:
        kategorija,slika = i.split(',')
        d[kategorija] = slika
    return render_template('index.html',kategorii = d)

@app.route('/<string:kategorija>')
def product(kategorija):
    print(kategorija)
    if 'Штраф' in kategorija:
        temp = (strafovi[strafovi.Ime.str.contains(kategorija)]).to_dict(orient='records')
        return render_template('product.html',name=kategorija,slika=d[kategorija],velicini=temp,kategorii=d.keys())
    elif 'Мутери' in kategorija:
        muteri_dict = muteri.to_dict(orient='records')
        return render_template('product.html',name=kategorija,slika=d[kategorija],velicini=muteri_dict,kategorii=d.keys())
    else:

        return '<h1> dasda </h1>'
if __name__ == '__main__':
    app.run(debug=True)



