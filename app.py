from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import random
import base64
from ocr import getData, processData, assess

app = Flask(__name__)

Bootstrap(app)

currWord = ""
wordslist = []

#home / home
@app.route("/")
def home():
    return render_template("home.html")

#about 
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/handwriting/', methods = ["GET", "POST"])
def handwriting():
    global currWord
    if request.method == "POST":
        reqjson = str(request.get_json())[22:]
        with open("image.png", "wb") as imgfile:
            imgfile.write(base64.b64decode(reqjson))
        writtenWord, characters = processData(getData('image.png'))
        res = assess(currWord, writtenWord)
        print(res)
        print(jsonify(res))
        return jsonify("OK")
    currWord = wordslist[random.randint(0, len(wordslist))].split(';')[0]
    definition = wordslist[random.randint(0, len(wordslist))].split(';')[1]
    return render_template("hwp.html", word = currWord, definition = definition)

@app.route('/games/')
def games():
    return render_template("games.html")

if __name__ == "__main__":
    with open("words.txt", "r") as readfile:
        wordslist = readfile.readlines()
    app.run(debug=True)