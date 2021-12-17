from flask import Flask,render_template,url_for,request



app = Flask(__name__)
with open('categories.txt') as cat:
    categories = cat.readlines()


@app.route('/')
def index():
    return render_template('index.html',categories = categories)


if __name__ == '__main__':
    app.run(debug=True)