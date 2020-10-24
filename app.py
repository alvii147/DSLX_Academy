from flask import Flask, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

#home / home
@app.route("/")
def home():
    return render_template("home.html")

#about 
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/handwriting/')
def handwriting():
    return render_template("hwp.html")

@app.route('/games/')
def games():
    return render_template("games.html")


if __name__ == "__main__":
    app.run(debug=True)