from flask import jsonify, Blueprint, request, current_app
from models.Game import Game
from services.GameManager import GameManager

save_bp = Blueprint('save', __name__, url_prefix='/api')

@save_bp.route("/save", methods=["POST"])
def saveGame():
    db = current_app.config["db"]
    game_manager = GameManager(db)
    data = request.get_json()

    game = Game(
        gameCode=None,
        name = data['gameName'],
        platform = data['platform_id'],
        score = data['score'],
        status = data['status_id']
    )

    resp, status = game_manager.create_game(game)
    return jsonify(resp), status

@save_bp.route("/games", methods=["GET"])
def getGame():
    db = current_app.config["db"]
    game_manager = GameManager(db)

    resp, status = game_manager.get_all_games()
    return jsonify(resp), status