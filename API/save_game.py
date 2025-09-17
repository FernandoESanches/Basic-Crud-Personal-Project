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
        platform = data['platform'],
        score = data['score'],
        status = data['status']
    )

    resp, status = game_manager.create_game(game)
    return jsonify(resp), status