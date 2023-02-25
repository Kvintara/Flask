

from flask import Flask, render_template, request, redirect, url_for, flash
from dictionary import data_game_l2
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/<string:title>")
def game(title):
    return render_template("game.html", title=title, data=data_game_l2)


@app.route("/music")
def music():
    return render_template("music.html", title="Music")


@app.route('/movie')
def movie():
    return render_template("movie.html", title="Movie")


@app.route('/book')
def book():
    return render_template("book.html", title="Book")


@app.route('/base')
def base():
    return render_template("base.html", title="Base")


if __name__ == "__main__":
    app.run(debug=True)
