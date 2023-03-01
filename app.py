

from flask import Flask, render_template, request, redirect, url_for, flash
from dictionary import data_game_l2, data_game_wow, data_game_totalwar, data_movie_uw, data_movie_uw_e, data_movie_uw_rotl, \
    data_movie_uw_a, data_movie_uw_bw, data_music_nirvana, data_music_am_foje, data_music_bm


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index(title):
    return render_template("index.html", title=title)


@app.route("/game<string:title>")
def game(title):
    return render_template("game.html", title=title, data_1=data_game_l2, data_2=data_game_wow, data_3=data_game_totalwar)


@app.route("/music<string:title>")
def music(title):
    return render_template("music.html", title=title, data_9=data_music_nirvana, data_10=data_music_am_foje, data_11=data_music_bm)


@app.route('/movie<string:title>')
def movie(title):
    return render_template("movie.html", title=title, data_4=data_movie_uw, data_5=data_movie_uw_e, data_6=data_movie_uw_rotl, data_7=data_movie_uw_a, data_8=data_movie_uw_bw)


@app.route('/book')
def book():
    return render_template("book.html", title="Book")


@app.route('/base')
def base():
    return render_template("base.html", title="Base")


if __name__ == "__main__":
    app.run(debug=True)
