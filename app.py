from flask import Flask
from flask import render_template
import flaskr.db as db
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def index():
    category = 1
    result = db.get_category(category)
    total = int(result[3])
    return render_template("index.html", total=total + 1, category=category)


@app.route("/show/<category>/<episode>")
def show(category, episode):
    cartoon = db.get_subtitle(category, episode)
    subtitles = str(cartoon[3]).split("\\n")
    return render_template("show.html", subtitles=subtitles, category_id=int(category), episode_id=int(episode))


if __name__ == '__main__':
    app.run()
