# -*- coding: utf-8 -*-
import spider
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/score", methods=["POST"])
def score():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    course_list = spider.getScore(username, password)
    length = len(course_list)
    return render_template("score.html", list=course_list, length=length)


if __name__ == '__main__':
    app.run(debug=True)
