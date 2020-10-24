from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")

# handwriting recognition page

# reading

# memory game page

if __name__ == "__main__":
    app.run()