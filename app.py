from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return f"<h1>idk something</h1>"

if __name__ == "__main__":
    app.run()