from flask import Flask
from flask import render_template
import flaskr.db as db
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/show/<cartoon_id>")
def show(cartoon_id):
    cartoon = db.get_cartoon(cartoon_id)
    subtitle = str(cartoon[2]).split(".")
    return render_template("show.html", cartoon=cartoon, subtitle=subtitle)


if __name__ == '__main__':
    app.run()
