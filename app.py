from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sys
app = Flask(__name__)
import database
import pandas as pd

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apply")
def apply():
    return render_template("apply.html")

@app.route("/applyphoto")
def applyphoto():
    userid = request.args.get("userid")
    database.save(userid)
    return render_template("applyphoto.html")

@app.route("/list")
def list():
    photo_list = database.load_list()
    length = len(photo_list)
    return render_template("list.html", photo_list = photo_list, length = length)

@app.route("/viewphoto", methods=["POST"])
def viewphoto():
    f = request.files["file"]
    f.save("static/img/{}.jpeg".format(database.now_index()))
    return render_template("viewphoto.html", img="img/{}.jpeg".format(database.now_index()))

@app.route("/photo_info/<int:index>/")
def photo_info(index):
    photo_info = database.load_photo(index)
    photo = f"img/{index}.jpeg"
    return render_template("photo_info.html", photo = photo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
