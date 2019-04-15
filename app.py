from flask import Flask

from flask import render_template

import flaskr.db as db

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/show/<cartoon_id>")
def show(cartoon_id):
    cartoon = db.get_cartoon(int(cartoon_id))
    return render_template("show.html")


if __name__ == '__main__':
    app.run()
