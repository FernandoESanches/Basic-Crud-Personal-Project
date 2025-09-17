from flask import Flask, render_template
from API.save_game import save_bp
from config import DbConfig
from db.Database import DataBase

app = Flask(__name__)
app.config.from_object(DbConfig)

db = DataBase(DbConfig.SQLALCHEMY_DATABASE_URI)
app.config["db"] = db
app.register_blueprint(save_bp)

@app.route("/")
def index():
    return render_template("homePage.html")

