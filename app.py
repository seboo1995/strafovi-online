from os import read, readlink
from flask import Flask,render_template,url_for




app = Flask(__name__)
with open('categories.txt') as cat:
    categories = cat.readlines()


@app.route('/')
def index():
    print(categories)
    return render_template('index.html',categories = categories)


if __name__ == '__main__':
    app.run(debug=True  )