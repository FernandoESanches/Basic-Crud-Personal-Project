from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from API.save_game import save_bp
from config import DbConfig

app = Flask(__name__)
app.config.from_object(DbConfig)

db = SQLAlchemy(app)
app.register_blueprint(save_bp)

@app.route("/")
def index():
    return render_template("homePage.html")

